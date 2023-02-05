import logging
import os
import time

from database import models, queries
from geo_handling import GeoEndpoint
from spotify import SpotifyClient

from .festival_formatter import Formatter
from .rating import Rating
from .spotify_data import SpotifyData

logger = logging.getLogger(__name__)


class Suggester(object):

    def __init__(self):
        self.rating = Rating()
        self.geo = GeoEndpoint(access_token=os.environ["ipinfo_access_token"])

    @staticmethod
    def get_spotify_data(authorization: str, ip: str, cookie: str) -> tuple[SpotifyData, models.SpotifyRequest]:
        req = models.SpotifyRequest(
            ip=ip,
            cookie=cookie,
        )
        req.save()
        logger.debug(f"Getting spotify data. Authorization: {authorization}")
        username = SpotifyClient.get_username(authorization)
        top_artists = SpotifyClient.get_top_artists(authorization, req)
        top_track_artists = SpotifyClient.get_top_track_artists(authorization, req)
        return SpotifyData(username, top_track_artists, top_artists), req

    @staticmethod
    def get_authorization(cookie: str) -> str:
        logger.debug(f"Getting authorization for cookie {cookie}")
        auth = queries.get_authorization(cookie)
        logger.debug(f"Authorization for cookie {cookie} is {auth}")
        return auth

    def get_suggestions(self, cookie: str, ip: str) -> tuple[list[dict], models.SpotifyRequest, str, str]:
        logger.info("User requested suggestions.")
        start = time.time()
        authorization = self.get_authorization(cookie)
        spotify_data, req = self.get_spotify_data(authorization, ip, cookie)
        user_location = self.geo.get_location_from_ip(ip, req)
        logger.info(f"Time for getting spotify data: {round(time.time()-start, 2)}")
        suggestions = self.rating.get_top_festivals(
            spotify_data.top_artists,
            spotify_data.top_track_artists,
            user_location,
            req
        )
        return Formatter.format(suggestions), req, spotify_data.username, user_location.city
