import logging
import os
from urllib.parse import urlencode

from database.models import SpotifyArtist, SpotifyRequest, SpotifyTrack

from .response_processor import ResponseProcessor
from .spotify_endpoint import SpotifyEndpoint

logger = logging.getLogger(__name__)


class SpotifyClient:

    @staticmethod
    def create_login_url() -> str:
        """Create a Spotify login URL."""
        logger.debug("Creating login URL.")
        return "https://accounts.spotify.com/authorize?" + urlencode({
            "response_type": "code",
            "client_id": os.environ["SPOTIFY_CLIENT_ID"],
            "scope": "user-top-read",
            "redirect_uri": f"{os.environ['WEBSITE_BACKEND_URL']}/api/authorize",
        })

    @staticmethod
    def authorize_user(cookie: str):
        auth_response = SpotifyEndpoint.get_user_auth_token(cookie)
        ResponseProcessor.save_authorization(auth_response, cookie)
        logger.info("User successfully authorized.")

    @staticmethod
    def get_username(user_auth: str) -> str:
        try:
            user_data = SpotifyEndpoint.get_user_data(user_auth)
            return ResponseProcessor.process_user_name(user_data)
        except Exception as e:
            return "You"

    @staticmethod
    def get_top_artists(user_auth: str, request: SpotifyRequest) -> list[SpotifyArtist]:
        artists = SpotifyEndpoint.get_top_n_items(user_auth, "artists")
        return ResponseProcessor.process_artists_response(artists, request)

    @staticmethod
    def get_top_track_artists(user_auth: str, request: SpotifyRequest) -> list[SpotifyArtist]:
        tracks = SpotifyEndpoint.get_top_n_items(user_auth, "tracks")
        return ResponseProcessor.process_tracks_response(tracks, request)
