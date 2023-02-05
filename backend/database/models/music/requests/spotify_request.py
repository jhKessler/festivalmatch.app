from peewee import AutoField, CharField

from ...base_model import BaseModel


class SpotifyRequest(BaseModel):
    id = AutoField()
    ip = CharField()
    cookie = CharField()
    