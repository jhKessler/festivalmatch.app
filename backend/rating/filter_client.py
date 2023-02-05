import logging

import pandas as pd

logger = logging.getLogger(__name__)


class FilterClient:

    @staticmethod
    def filter_festivals(appearances: pd.DataFrame, festivals: pd.DataFrame, relevant_artists: set[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
        logger.debug("Getting relevant festivals")
        relevant_appearances = appearances[appearances["artist_id"].isin(relevant_artists)]
        relevant_festivals = festivals[festivals["id"].isin(relevant_appearances["festival_id"].unique())]
        logger.debug("Finished getting relevant festivals")
        return relevant_festivals
        