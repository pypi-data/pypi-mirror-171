import logging
from typing import List
import numba
import numpy as np
from matchms.typing import SpectrumType
from .BaseSimilarity import BaseSimilarity


logger = logging.getLogger("matchms")


class MetadataMatch(BaseSimilarity):
    """Return True if metadata entries of a specified field match between two spectra.

    This is supposed to be used to compare a wide range of possible metadata entries and
    use this to later select related or similar spectra.

    Example to calculate scores between 2 pairs of spectrums and iterate over the scores

    .. testcode::

        import numpy as np
        from matchms import calculate_scores
        from matchms import Spectrum
        from matchms.similarity import MetadataMatch

        spectrum_1 = Spectrum(mz=np.array([]),
                              intensities=np.array([]),
                              metadata={"instrument_type": "orbitrap",
                                        "id": 1})
        spectrum_2 = Spectrum(mz=np.array([]),
                              intensities=np.array([]),
                              metadata={"instrument_type": "qtof",
                                        "id": 2})
        spectrum_3 = Spectrum(mz=np.array([]),
                              intensities=np.array([]),
                              metadata={"instrument_type": "qtof",
                                        "id": 3})
        spectrum_4 = Spectrum(mz=np.array([]),
                              intensities=np.array([]),
                              metadata={"instrument_type": "orbitrap",
                                        "id": 4})
        references = [spectrum_1, spectrum_2]
        queries = [spectrum_3, spectrum_4]

        similarity_score = MetadataMatch(field="instrument_type")
        scores = calculate_scores(references, queries, similarity_score)

        for (reference, query, score) in scores:
            print(f"Metadata match between {reference.get('id')} and {query.get('id')}" +
                  f" is {score:.2f}")

    Should output

    .. testoutput::

        Metadata match between 1 and 3 is 0.00
        Metadata match between 1 and 4 is 1.00
        Metadata match between 2 and 3 is 1.00
        Metadata match between 2 and 4 is 0.00

    """
    # Set key characteristics as class attributes
    is_commutative = True
    score_datatype = bool

    def __init__(self, field: str,
                 matching_type: str = "equal_match",
                 tolerance: float = 0.1):
        """
        Parameters
        ----------
        field
            Specify field name for metadata that should be compared.
        matching_type
            Specify how field entries should be matched. Can be one of
            ["equal_match", "difference"].
        tolerance
            Specify tolerance below which two values are counted as match.
            This only applied to numerical values.
        """
        self.field = field
        self.tolerance = tolerance
        assert matching_type in ["equal_match", "difference"], \
            "Expected type from ['equal_match', 'difference']"
        self.matching_type = matching_type

    def pair(self, reference: SpectrumType, query: SpectrumType) -> float:
        """Compare precursor m/z between reference and query spectrum.

        Parameters
        ----------
        reference
            Single reference spectrum.
        query
            Single query spectrum.
        """
        entry_ref = reference.get(self.field)
        entry_query = query.get(self.field)
        if entry_ref is None or entry_query is None:
            return np.asarray(False, dtype=self.score_datatype)

        if self.matching_type == "equal_match":
            score = (entry_ref == entry_query)
            return np.asarray(score, dtype=self.score_datatype)

        if isinstance(entry_ref, (int, float)) and isinstance(entry_query, (int, float)):
            score = abs(entry_ref - entry_query) <= self.tolerance
            return np.asarray(score, dtype=self.score_datatype)

        logger.warning("Non-numerical entry not compatible with 'difference' method")
        return np.asarray(False, dtype=self.score_datatype)

    def matrix(self, references: List[SpectrumType], queries: List[SpectrumType],
               is_symmetric: bool = False) -> np.ndarray:
        """Compare parent masses between all references and queries.

        Parameters
        ----------
        references
            List/array of reference spectrums.
        queries
            List/array of Single query spectrums.
        is_symmetric
            Set to True when *references* and *queries* are identical (as for instance for an all-vs-all
            comparison). By using the fact that score[i,j] = score[j,i] the calculation will be about
            2x faster.
        """
        def collect_entries(spectrums):
            """Collect metadata entries."""
            entries = []
            for spectrum in spectrums:
                entry = spectrum.get(self.field)
                if entry is None:
                    msg = f"No {self.field} entry found for spectrum."
                    logger.warning(msg)
                    entry = np.nan
                elif self.matching_type == "difference" and not isinstance(entry, (int, float)):
                    msg = f"Non-numerical entry ({entry}) not compatible with 'difference' method."
                    logger.warning(msg)
                    entry = np.nan
                entries.append(entry)
            return np.asarray(entries)

        entries_ref = collect_entries(references)
        entries_query = collect_entries(queries)

        if self.matching_type == "equal_match":
            scores = np.zeros((len(entries_ref), len(entries_query)))
            for i, entry in enumerate(entries_query):
                idx = np.where(entries_ref == entry)
                scores[idx, i] = 1
            return scores.astype(self.score_datatype)

        if is_symmetric:
            return entries_scores_symmetric(entries_ref, entries_query,
                                            self.tolerance).astype(self.score_datatype)
        return entries_scores(entries_ref, entries_query,
                              self.tolerance).astype(self.score_datatype)


@numba.njit
def entries_scores(entries_ref, entries_query, tolerance):
    scores = np.zeros((len(entries_ref), len(entries_query)))
    for i, entry_ref in enumerate(entries_ref):
        for j, entry_query in enumerate(entries_query):
            scores[i, j] = (abs(entry_ref - entry_query) <= tolerance)
    return scores


@numba.njit
def entries_scores_symmetric(entries_ref, entries_query, tolerance):
    scores = np.zeros((len(entries_ref), len(entries_query)))
    for i, entry_ref in enumerate(entries_ref):
        for j in range(i, len(entries_query)):
            scores[i, j] = (abs(entry_ref - entries_query[j]) <= tolerance)
            scores[j, i] = scores[i, j]
    return scores
