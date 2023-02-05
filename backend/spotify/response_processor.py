import logging

from database.models import SpotifyArtist, SpotifyRequest, UserAuthorization

from .item_processor import ItemProcessor

logger = logging.getLogger(__name__)


class ResponseProcessor(object):

    @staticmethod
    def save_authorization(authorization_response: dict, cookie: str) -> UserAuthorization:
        UserAuthorization.from_response(authorization_response, cookie)

    @staticmethod
    def process_user_name(response: dict) -> str:
        logger.debug("Processing user name")
        return response["display_name"]

    @staticmethod
    def process_artists_response(response: dict, request: SpotifyRequest) -> list[SpotifyArtist]:
        logger.debug("Processing artists response")
        return [
            ItemProcessor.process_artist_item(item, rank, request) for rank, item in enumerate(response["items"])
        ]

    @staticmethod
    def process_tracks_response(response: dict, request: SpotifyRequest) -> list[SpotifyArtist]:
        song_artists = [
            ItemProcessor.process_track_item(item, rank, request) for rank, item in enumerate(response["items"])
        ]
        return [artist for artists in song_artists for artist in artists]
