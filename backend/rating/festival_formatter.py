import pandas as pd


class Formatter:

    @staticmethod
    def format(festivals: pd.DataFrame) -> list[dict]:
        return festivals[["name", "date", "location", "website", "lineup"]].to_dict(orient="records")
        