import logging

from peewee import BooleanField, CharField, DateTimeField, IntegerField

from ...base_model import BaseModel

logger = logging.getLogger(__name__)

class SpotifyTrack(BaseModel):

    def __str__(self):
        return f"SpotifyTrack(id={self.id}, name={self.name})"

    @staticmethod
    def from_item(item: dict) -> "SpotifyTrack":
        logger.debug(f"Creating SpotifyTrack from item: {item}")
        instance = SpotifyTrack(
            id=item["id"],
            name=item["name"],
            popularity=item["popularity"],
            album_type=item["album"]["album_type"],
            release_date=item["album"]["release_date"],
            track_number=item["track_number"],
            duration_ms=item["duration_ms"],
            explicit=item["explicit"]
        )
        return instance

    id = CharField(primary_key=True)
    name = CharField()
    popularity = IntegerField()
    duration_ms = IntegerField()
    explicit = BooleanField()
    album_type = CharField()
    release_date = CharField()
    track_number = IntegerField()
