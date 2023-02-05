import re
import os
import base64
import requests

class SpotifyEndpoint:

    @staticmethod
    def request_self_token() -> dict:
        message = f"{os.environ['SPOTIFY_CLIENT_ID']}:{os.environ['SPOTIFY_CLIENT_SECRET']}"
        messagebase64 = base64.b64encode(message.encode())
        data={
            "grant_type": "client_credentials",
        }
        token_header={
            "Authorization": f"Basic {messagebase64.decode()}"
        }
        r = requests.post('https://accounts.spotify.com/api/token', data=data, headers=token_header)
        return r.json()

    @staticmethod
    def search_artist_by_name(name: str, token: str) -> requests.Response:
        """Search for an artist by name.

        Args:
            name (str): Name of the artist to search for.
            token (str): Authentication token.

        Returns:
            dict: JSON response from the Spotify API.
        """
        name = re.sub(r"[\.\- ]", "", name).lower().strip()
        res = requests.get(
            f"https://api.spotify.com/v1/search?query={name}&type=artist&limit=20",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )
        return res

    @staticmethod
    def process_artist_search_response(queried_name: str, response: dict) -> dict:
        try:
            items = response["artists"]["items"]
            for artist in items:
                if artist["name"].lower() == queried_name.lower():
                    print(f"Found artist {artist['name']} (query: {queried_name})")
                    return artist
            print(f"No exact match for artist {queried_name}, skipping...")
            return None
        except KeyError as e:
            print("No artist found")
            print(response)
            raise e
