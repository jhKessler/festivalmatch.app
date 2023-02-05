from peewee import CharField, ForeignKeyField, IntegerField

from ...base_model import BaseModel
from .spotify_request import SpotifyRequest


class TrackRequest(BaseModel):

    request_id = ForeignKeyField(SpotifyRequest)
    track_id = CharField()
    rank = IntegerField()
