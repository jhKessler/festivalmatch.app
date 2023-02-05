from peewee import CharField, FloatField, ForeignKeyField, IntegerField

from ...base_model import BaseModel
from ..requests import SpotifyRequest
from ..spotify.spotify_artist import SpotifyArtist
from .festival import Festival


class ArtistRanking(BaseModel):
    suggestion_id = ForeignKeyField(SpotifyRequest)
    festival_id = ForeignKeyField(Festival)
    artist_id = ForeignKeyField(SpotifyArtist)
    rank = IntegerField()
    value = FloatField()
    type = CharField()
