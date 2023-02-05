from peewee import ForeignKeyField

from ...base_model import BaseModel
from ..spotify.spotify_artist import SpotifyArtist
from .festival import Festival


class FestivalAppearance(BaseModel):
    
    artist_id = ForeignKeyField(SpotifyArtist)
    festival_id = ForeignKeyField(Festival)
