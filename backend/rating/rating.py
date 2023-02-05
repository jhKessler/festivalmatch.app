import os
import logging
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, engine
from database.models import SpotifyArtist, ArtistRanking, SpotifyRequest, UserLocation
from .filter_client import FilterClient
from geo_handling import GeoCalculator

logger = logging.getLogger(__name__)

class Rating:

    @staticmethod
    def get_artist_score_ranking() -> list[float]:
        artist_scores = np.arange(200, 500, 6) ** 2
        artist_scores = artist_scores / artist_scores.max()
        artist_scores = np.maximum(artist_scores, 0.2)
        artist_scores[-10:] *= 2
        return artist_scores[::-1]

    @staticmethod
    def get_engine() -> engine:
        return create_engine(
            f"postgresql://{os.environ['user']}:{os.environ['password']}@{os.environ['host']}:{os.environ['port']}/{os.environ['database']}"
        )

    def get_festival_rating(
            self,
            festival: pd.Series, 
            top_artists: list[SpotifyArtist], 
            top_tracks_artists: list[SpotifyArtist],
            user_location: UserLocation,
            req: SpotifyRequest
        ) -> pd.Series:
        logger.debug(f"Getting festival rating for festival {festival['name']}")
        festival_appearances = set(self.appearances_by_festival.get_group(festival["id"])["artist_id"])
        scores = self.get_artist_matches(top_artists, festival_appearances, type="top_artists", req=req, festival_id=festival["id"])
        scores.extend(self.get_artist_matches(top_tracks_artists, festival_appearances, type="top_tracks_artists", req=req, festival_id=festival["id"]))
        scores = pd.DataFrame.from_records(scores)
        artist_scores = scores.groupby("name")["value"].sum()
        distance_km = GeoCalculator.get_distance_km((user_location.latitude, user_location.longitude), (festival["latitude"], festival["longitude"]))
        distance_mult = max(1, distance_km // 200)
        return pd.Series({
            "lineup": artist_scores.sort_values(ascending=False).index.tolist(),
            "score_no_distance": artist_scores.sum(),
            "distance": distance_km,
            "score_distance": artist_scores.sum() / distance_mult
        })

    def get_artist_matches(self, top_artists: list[SpotifyArtist], festival_appearances: set[str], type: str, req: SpotifyRequest, festival_id: int) -> list[dict]:
        logger.debug(f"Getting artist matches for {type}")
        artist_matches = []
        for rank, artist in enumerate(top_artists):
            if artist.id in festival_appearances:
                value = self.rank_values[rank] if type == "top_artists" else 0.1
                artist_matches.append({
                    "name": artist.name,
                    "id": artist.id,
                    "rank": rank,
                    "value": value,
                })
                logger.debug(f"Saving artist {artist.name} with rank {rank} and value {value}")
                ArtistRanking(
                    suggestion_id=req.id,
                    artist_id=artist.id,
                    rank=rank,
                    value=value,
                    type=type,
                    festival_id=festival_id
                ).save()
                logger.debug(f"Saved artist {artist.name} with rank {rank} and value {value}")
        logger.debug(f"Found {artist_matches} matches for {type}")
        return artist_matches
    
    def __init__(self) -> None:
        self.con = Rating.get_engine()
        logger.info("Loading appearances and festivals from database")
        self.appearances = pd.read_sql_table("festivalappearance", self.con).merge(
            pd.read_sql_table("spotifyartist", self.con), 
            left_on="artist_id", right_on="id"
        )
        self.festivals = pd.read_sql_table("festival", self.con)
        self.appearances_by_festival = self.appearances.groupby("festival_id")
        logger.info("Finished loading appearances and festivals from database")
        self.rank_values = Rating.get_artist_score_ranking()

    def add_unmatched_artists_to_row(self, row: pd.Series) -> pd.Series:
        artists = set(row["lineup"])
        appearances_in_festival = self.appearances[self.appearances["festival_id"] == row.id]["name"]
        while len(row["lineup"]) < min(12, len(appearances_in_festival)):
            random_artist_from_festival = appearances_in_festival.sample(1).iloc[0]
            if random_artist_from_festival not in artists:
                artists.add(random_artist_from_festival)
                row["lineup"].append(random_artist_from_festival)
        return row

    def add_unmatched_artists(self, top: pd.DataFrame) -> pd.DataFrame:
        return top.apply(lambda row: self.add_unmatched_artists_to_row(row), axis=1)

    def get_top_festivals(self, top_artists: list[SpotifyArtist], top_tracks_artists: list[SpotifyArtist], user_location: UserLocation, req: SpotifyRequest) -> pd.DataFrame:
        relevant_artists = {artist.id for artist in (top_artists+top_tracks_artists)}
        festivals = FilterClient.filter_festivals(
            self.appearances, 
            self.festivals, 
            relevant_artists
        )
        top_artists = [artist for artist in top_artists if artist.id in relevant_artists]
        top_tracks_artists = [artist for artist in top_tracks_artists if artist.id in relevant_artists]
        festivals = pd.concat([festivals, festivals.apply(
            lambda festival: self.get_festival_rating(festival, top_artists, top_tracks_artists, user_location, req),
            axis=1
        )], axis=1)

        top = festivals.sort_values("score_distance", ascending=False).iloc[:10]
        return self.add_unmatched_artists(top)
