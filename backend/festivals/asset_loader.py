import pandas as pd


class AssetLoader:

    @staticmethod
    def load_festivals() -> pd.DataFrame:
        return pd.read_csv("festivals/assets/festivals.csv")

    @staticmethod
    def load_artists() -> pd.DataFrame:
        return pd.read_csv("festivals/assets/artists.csv")

    @staticmethod
    def load_appearances() -> pd.DataFrame:
        return pd.read_csv("festivals/assets/artist_appearances.csv")
