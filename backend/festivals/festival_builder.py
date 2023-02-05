import logging

import pandas as pd
from database.models import Festival, FestivalAppearance, SpotifyArtist

from .asset_loader import AssetLoader

logger = logging.getLogger(__name__)

class FestivalBuilder:

    def __init__(self) -> None:
        logger.info("Building festival database...")
        self.build()    
        logger.info("Finished building festival database")    

    def build(self) -> None:
        if FestivalAppearance.select().count():
            logger.info("Database already populated. Skipping...")
            return

        self.build_artists()
        self.build_festival_table()

    def build_artists(self) -> None:
        artists: pd.DataFrame = AssetLoader.load_artists()
        logger.info("Building artist table...")
        for _, artist in artists.iterrows():
            logger.debug(f"Adding artist {artist['name']}")
            SpotifyArtist.from_row(artist)

    def build_festival_table(self) -> None:
        festivals = AssetLoader.load_festivals()
        appearances = AssetLoader.load_appearances()

        logger.info("Building festival table...")
        for _, festival in festivals.iterrows():
            festival = Festival.from_series(festival, save=True)
            logger.debug(f"Adding appearances for festival {festival.name}")
            festival_appearances = appearances[appearances["festival"] == festival.name]
            for _, appearance in festival_appearances.iterrows():
                logger.debug(f"Adding appearance for artist {appearance['artist_id']}")
                FestivalAppearance(festival_id=festival.id,
                                   artist_id=appearance["artist_id"]).save()
                                   
