import tqdm
from src import FestivalParser, SpotifyEndpoint
import time
import pandas as pd


festivals = FestivalParser.parse_festivals()

all_artists = set()
for artists in festivals["lineup"]:
    all_artists.update(set(artists))

results = []

for index, artist in enumerate(list(all_artists)):
    time.sleep(0.2)
    if index % 100 == 0:
        print(f"Processing artist {index} of {len(all_artists)}")
    if index % 1000 == 0:
        token = SpotifyEndpoint.request_self_token()["access_token"]
        pd.DataFrame(results).to_csv("test.csv")
    res = SpotifyEndpoint.search_artist_by_name(artist, token)
    if res.status_code == 429:
        print(f"Rate limit exceeded, waiting {res.headers['Retry-After']} seconds")
        time.sleep(int(res.headers["Retry-After"])+1)
        res = SpotifyEndpoint.search_artist_by_name(artist, token)
    try:
        results.append({
            "query": artist,
            "result": SpotifyEndpoint.process_artist_search_response(artist, res.json())
        })
    except KeyError:
        print(f"Artist '{artist}' not found")

cleaned_artists = []
artist_mapping = {}

for q in tqdm(results):
    if q["result"] is None:
        continue
    row = q["result"]
    artist_id = row["id"]
    artist_name = row["name"]
    artist_popularity = row["popularity"]
    artist_followers = row["followers"]["total"]
    artist_mapping[q["query"]] = artist_id
    cleaned_artists.append({
        "id": artist_id,
        "name": artist_name,
        "popularity": artist_popularity,
        "followers": artist_followers
    })

pd.DataFrame(cleaned_artists).to_csv("artists.csv", index=False)

festivals["artist_count"] = festivals["lineup_ids"].str.len()
festivals = festivals[(festivals["artist_count"] > 7)]
festivals["lineup_ids"] = festivals["lineup"].apply(lambda artists: [artist_mapping[a] for a in artists if a in artist_mapping])
festivals["artist_count"] = festivals["lineup_ids"].str.len()
festivals["location"] = festivals["location"].str.split(",", 1).str[-1]


artist_appearances = []
for _, festival in festivals.iterrows():
    for artist in festival["lineup_ids"]:
        artist_appearances.append({
            "artist_id": artist,
            "festival": festival["name"],
        })

pd.DataFrame(artist_appearances).to_csv("artist_appearances.csv", index=False)
festivals.drop(columns=["lineup_ids", "lineup", "artist_count", "country"]).to_csv("festivals.csv", index=False)