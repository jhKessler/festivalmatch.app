from ..base_model import BaseModel
from peewee import CharField, ForeignKeyField, DateTimeField
from playhouse.postgres_ext import JSONField

class UserEvent(BaseModel):
    timestamp = DateTimeField()
    ip = CharField()
    event_type = CharField()
    headers = JSONField()
