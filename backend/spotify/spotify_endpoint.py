import logging
import os

import requests

logger = logging.getLogger(__name__)


class SpotifyEndpoint:

    @staticmethod
    def get_user_data(user_auth: str) -> dict:
        """Request the User profile from the Spotify API.

        Args:
            user_auth (str): User authentication token.

        Returns:
            dict: JSON response from the Spotify API.
        """
        logger.debug(f"Getting user data for user auth {user_auth}")
        res = requests.get(
            "https://api.spotify.com/v1/me",
            headers={
                "Authorization": f"Bearer {user_auth}",
                "Content-Type": "application/json"
            }
        ).json()
        logger.debug(f"User data response: {res}")
        if "error" in res:
            logger.error("error in user data response: ", res["error"])
            raise Exception(res["error"])
        return res

    @staticmethod
    def get_user_auth_token(cookie: str) -> dict:
        """Get a User authentication token from the Spotify API.

        Args:
            code (str): Code from the Spotify callback.

        Returns:
            str: User authentication token.
        """
        logger.debug(f"Getting user auth token for cookie {cookie}")
        res = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": cookie,
                "redirect_uri": f"{os.environ['WEBSITE_BACKEND_URL']}/api/authorize"
            },
            headers={
                "Authorization": f"Basic {os.environ['SPOTIFY_CLIENT_AUTH_STR']}"
            }
        ).json()
        logger.debug(f"User auth token response: {res}")
        if "error" in res:
            logger.error("error in user auth token response: ", res["error"])
            raise Exception(res["error"])
        return res

    @staticmethod
    def get_top_n_items(user_auth: str, item_type: str, n: int = 50) -> dict:
        """Request the top n items of a User from the Spotify API.

        Args:
            user_auth (str): User authentication token.
            n (int): Number of items to request.
            item_type (str): Type of item to request. Can be 'tracks' or 'artists'.

        Returns:
            dict: JSON response from the Spotify API.
        """
        logger.debug(f"Getting top {n} {item_type} for user auth {user_auth}")
        res = requests.get(
            f"https://api.spotify.com/v1/me/top/{item_type}?limit={n}&time_range=medium_term",
            headers={
                "Authorization": f"Bearer {user_auth}",
                "Content-Type": "application/json"
            }
        ).json()
        logger.debug(f"Top {n} {item_type} response: {res}")
        if "error" in res:
            logger.error(f"error in top {n} {item_type} response: ", res["error"])
            raise Exception(res["error"])
        return res
