import logging
import time

from .models import FestivalSuggestion, SpotifyRequest, all_entities
from .models.base_model import db

logger = logging.getLogger(__name__)

class Database:

    def __init__(self) -> None:
        self.db = db
        logger.debug("Connecting to database...")
        time.sleep(1) # wait for db to start
        self.db.connect()
        logger.debug("Connected to database")
        logger.debug("Creating tables...")
        self.db.create_tables(all_entities)
        logger.debug("Created tables")
