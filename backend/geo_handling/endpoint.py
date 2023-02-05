import logging
import os

import ipinfo
from database.models import SpotifyRequest, UserLocation

logger = logging.getLogger(__name__)


class GeoEndpoint:

    def __init__(self, access_token: str) -> None:
        self.handler = ipinfo.getHandler(access_token)

    def get_location_from_ip(self, ip_address: str, req: SpotifyRequest) -> UserLocation:
        logger.debug(f"Getting location from ip {ip_address}")
        details = self.handler.getDetails(ip_address).all
        location = UserLocation.from_response(details, req)
        logger.info(f"User location: {location.city}")
        location.save()
        return location
