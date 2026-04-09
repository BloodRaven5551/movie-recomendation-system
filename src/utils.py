import requests
import pandas as pd

API_KEY = "39276e2761db2a5dfca927607dd76ed3"

poster_cache = {}

PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Poster"

def fetch_poster(tmdb_id):
    if pd.isna(tmdb_id):
        return PLACEHOLDER

    tmdb_id = int(tmdb_id)

    if tmdb_id in poster_cache:
        return poster_cache[tmdb_id]

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

    try:
        res = requests.get(url, timeout=3)

        if res.status_code != 200:
            return PLACEHOLDER

        data = res.json()
        path = data.get("poster_path")

        poster = f"https://image.tmdb.org/t/p/w500{path}" if path else PLACEHOLDER

        poster_cache[tmdb_id] = poster
        return poster

    except:
        return PLACEHOLDER