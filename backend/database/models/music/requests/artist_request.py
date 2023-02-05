from peewee import CharField, ForeignKeyField, IntegerField

from ...base_model import BaseModel
from .spotify_request import SpotifyRequest


class ArtistRequest(BaseModel):

    request_id = ForeignKeyField(SpotifyRequest)
    artist_id = CharField()
    rank = IntegerField()
