from peewee import ForeignKeyField

from ...base_model import BaseModel
from .spotify_artist import SpotifyArtist
from .spotify_track import SpotifyTrack


class ArtistTrack(BaseModel):
    artist_id = ForeignKeyField(SpotifyArtist)
    track_id = ForeignKeyField(SpotifyTrack)
