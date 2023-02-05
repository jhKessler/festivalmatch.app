from dataclasses import dataclass

from database.models import SpotifyArtist, SpotifyTrack


@dataclass
class SpotifyData:

    username: str
    top_track_artists: list[SpotifyTrack]
    top_artists: list[SpotifyArtist]
