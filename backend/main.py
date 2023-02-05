import logging
import os
import time

import uvicorn
from database import queries
from database.models import FestivalSuggestion
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from init_backend import init_backend
from rating import Suggester
from spotify import SpotifyClient
from starlette.responses import RedirectResponse

init_backend()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger = logging.getLogger(__name__)

suggester = Suggester()


@app.get("/api/login")
async def login_user(request: Request):
    logger.info("User requested login.")
    return RedirectResponse(url=SpotifyClient.create_login_url())


@app.get("/api/authorize")
async def authorize_user(request: Request):
    logger.info("User requested authorization.")
    cookie = request.query_params['code']
    try:
        SpotifyClient.authorize_user(cookie)
    except Exception as e:
        logger.error("Error authorizing user: ", e)
        return RedirectResponse(url=f"{os.environ['WEBSITE_FRONTEND_URL']}/error")
    return RedirectResponse(url=f"{os.environ['WEBSITE_FRONTEND_URL']}/suggestions?code={cookie}")


@app.get("/api/festivals")
async def get_suggestions(request: Request):
    start = time.time()
    ip = request.headers.get("X-Forwarded-For", "92.74.175.205") # default to hamburg
    logger.info(f"User requested suggestions from {ip}.")
    suggestions, spotify_request, username, city = suggester.get_suggestions(
        cookie=request.query_params['cookie'],
        ip=ip
    )
    logger.info(f"Time for generating suggestions: {round(time.time()-start, 2)}")
    dump = {
        "status": "success",
        "suggestions": suggestions
    }
    dump["hash"] = FestivalSuggestion.dump(dump, spotify_request)
    logger.info(f"Generated {len(suggestions)} suggestions for user {username}.")
    return dump


@app.get("/api/shared")
async def get_shared_suggestions(request: Request):
    suggestions = queries.get_shared_suggestions(request.query_params['hash'])
    suggestions["hash"] = request.query_params['hash']
    return suggestions


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
