from __future__ import annotations

import logging
from datetime import datetime

from peewee import CharField, DateTimeField

from ..base_model import BaseModel

logger = logging.getLogger(__name__)

class UserAuthorization(BaseModel):

    @staticmethod
    def from_response(response: dict, cookie: str) -> UserAuthorization:
        logger.debug("Creating UserAuthorization from response")
        instance = UserAuthorization.create(
            cookie=cookie,
            access_token=response["access_token"],
            token_type=response["token_type"],
            expires_in=response["expires_in"],
            refresh_token=response["refresh_token"],
            scope=response["scope"],
        )
        logger.debug("Saving UserAuthorization")
        instance.save()
        logger.debug("Successfully saved UserAuthorization")
        return instance

    cookie = CharField()
    authorization_time = DateTimeField(default=datetime.now)
    access_token = CharField()
    token_type = CharField()
    refresh_token = CharField()
    scope = CharField()
