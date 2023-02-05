from .music import (
    ArtistRequest,
    SpotifyRequest,
    TrackRequest,
    SpotifyArtist,
    SpotifyTrack,
    ArtistTrack,
    Festival,
    FestivalAppearance,
    ArtistRanking,
    FestivalSuggestion
)

from .user import (
    UserAuthorization,
    UserEvent,
    UserLocation
)

all_entities = [
    ArtistRequest,
    SpotifyRequest,
    TrackRequest,
    SpotifyArtist,
    SpotifyTrack,
    ArtistTrack,
    Festival,
    FestivalAppearance,
    UserAuthorization,
    ArtistRanking,
    FestivalSuggestion,
    UserEvent,
    UserLocation
]
