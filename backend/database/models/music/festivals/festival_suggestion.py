import logging
import random
import string

from peewee import CharField, ForeignKeyField
from playhouse.postgres_ext import JSONField

from ...base_model import BaseModel
from ..requests import SpotifyRequest

logger = logging.getLogger(__name__)

class FestivalSuggestion(BaseModel):
    
    @staticmethod
    def generate_hash() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    @staticmethod
    def dump(suggestions_dump: dict, request: SpotifyRequest) -> str:
        logger.debug(f"Saving suggestion {request.ip}")
        hash = FestivalSuggestion.generate_hash()
        suggestion = FestivalSuggestion(
            request_id=request,
            hash=hash,
            data=suggestions_dump
        )
        suggestion.save(force_insert=True)
        logger.debug(f"Saved suggestion {request.ip}")
        return hash

    request_id = ForeignKeyField(SpotifyRequest, primary_key=True)
    hash = CharField()
    data = JSONField()
