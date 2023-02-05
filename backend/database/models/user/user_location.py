from __future__ import annotations

from peewee import BooleanField, CharField, FloatField, ForeignKeyField

from ..base_model import BaseModel
from ..music import SpotifyRequest


class UserLocation(BaseModel):

    def __str__(self) -> str:
        return f"UserLocation(ip={self.ip}, city={self.city}, country={self.country}"

    @staticmethod
    def from_response(response: dict, request: SpotifyRequest) -> UserLocation:
        return UserLocation(
            request_id=request.id,
            ip=response["ip"],
            city=response["city"],
            region=response["region"],
            country=response["country"],
            country_name=response["country_name"],
            is_eu=response["isEU"],
            continent_name=response["continent"]["name"],
            latitude=float(response["latitude"]),
            longitude=float(response["longitude"]),
        )

    request_id = ForeignKeyField(SpotifyRequest)
    ip = CharField()
    city = CharField()
    region = CharField()
    country = CharField()
    country_name = CharField()
    is_eu = BooleanField()
    continent_name = CharField()
    latitude = FloatField()
    longitude = FloatField()
