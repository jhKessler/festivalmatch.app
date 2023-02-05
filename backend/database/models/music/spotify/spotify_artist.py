from __future__ import annotations

import logging

import pandas as pd
from peewee import CharField, IntegerField

from ...base_model import BaseModel

logger = logging.getLogger(__name__)

class SpotifyArtist(BaseModel):

    def __str__(self):
        return f"SpotifyArtist(id={self.id}, name={self.name})"

    @staticmethod
    def from_row(row: pd.Series) -> SpotifyArtist:
        logger.debug(f"Creating SpotifyArtist from row: {row}")
        instance = SpotifyArtist(
            id=row["id"],
            name=row["name"],
            popularity=row.get("popularity"),
            followers=row.get("followers")
        )
        logger.debug(f"Saving SpotifyArtist: {instance}")
        instance.save(force_insert=True)
        logger.debug(f"Saved SpotifyArtist: {instance}")
        return instance


    @staticmethod
    def from_item(item: dict) -> SpotifyArtist:
        logger.debug(f"Creating SpotifyArtist from item: {item}")
        instance = SpotifyArtist(
            id=item.get("id"),
            name=item.get("name"),
            popularity=item.get("popularity"),
            followers=item.get("followers").get("total") if item.get("followers") else None
        )
        return instance

    id = CharField(primary_key=True)
    name = CharField()
    popularity = IntegerField(null=True)
    followers = IntegerField(null=True)
