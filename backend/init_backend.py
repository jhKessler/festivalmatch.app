import base64
import logging
import os
import time

from database import Database
from festivals import FestivalBuilder


def init_env():
    os.environ["SPOTIFY_CLIENT_AUTH_STR"] = base64.b64encode(
        f"{os.environ['SPOTIFY_CLIENT_ID']}:{os.environ['SPOTIFY_CLIENT_SECRET']}".encode()
    ).decode("utf-8")


def init_timezone():
    # if is unix
    if os.name == "posix":
        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(name)s %(threadName)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("festivalmatch.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


def init_database():
    Database()
    FestivalBuilder()


def init_backend():
    init_env()
    init_timezone()
    init_logging()
    init_database()


if __name__ == "__main__":
    init_backend()
