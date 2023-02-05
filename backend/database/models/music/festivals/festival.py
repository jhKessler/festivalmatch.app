from __future__ import annotations

import logging

import pandas as pd
from peewee import AutoField, CharField, FloatField

from ...base_model import BaseModel

logger = logging.getLogger(__name__)

class Festival(BaseModel):

    @staticmethod
    def from_series(series: pd.Series, save: bool) -> Festival:
        logger.debug(f"Creating Festival from series: {series}")
        instance = Festival(
            name=series["name"],
            date=series["date"],
            location=series["location"],
            website=series["website"],
            latitude=series["latitude"],
            longitude=series["longitude"]
        )
        if save:
            logger.debug(f"Saving Festival: {instance}")
            instance.save()
            logger.debug(f"Saved Festival: {instance}")
        return instance

    id = AutoField()
    name = CharField()
    date = CharField()
    location = CharField()
    website = CharField()
    latitude = FloatField()
    longitude = FloatField()
