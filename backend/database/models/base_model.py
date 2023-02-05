import os

from peewee import Model, PostgresqlDatabase

db = PostgresqlDatabase(
    database=os.environ.get("database") or "festival_db",
    user=os.environ.get("user") or "festival_db",
    password=os.environ.get("password") or "lennsucc56569976",
    host=os.environ.get("host") or "localhost",
    port=os.environ.get("port") or "5432",
    autorollback=True
)

class BaseModel(Model):
    class Meta:
        database = db
