from .models import FestivalSuggestion, UserAuthorization


def get_authorization(cookie: str) -> str:
    return UserAuthorization.get(UserAuthorization.cookie == cookie).access_token

def get_shared_suggestions(hash: str) -> dict:
    return FestivalSuggestion.get(FestivalSuggestion.hash == hash).data
    