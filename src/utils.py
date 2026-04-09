import requests
import pandas as pd

API_KEY = "39276e2761db2a5dfca927607dd76ed3"

poster_cache = {}

def fetch_poster(tmdb_id):
    if pd.isna(tmdb_id):
        return "https://via.placeholder.com/300x450?text=No+Image"

    tmdb_id = int(tmdb_id)

    if tmdb_id in poster_cache:
        return poster_cache[tmdb_id]

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

    try:
        res = requests.get(url, timeout=3)

        if res.status_code != 200:
            return "https://via.placeholder.com/300x450?text=No+Image"

        data = res.json()
        path = data.get("poster_path")

        if path:
            poster = f"https://image.tmdb.org/t/p/w500{path}"
        else:
            poster = "https://via.placeholder.com/300x450?text=No+Image"

        poster_cache[tmdb_id] = poster
        return poster

    except:
        return "https://via.placeholder.com/300x450?text=No+Image"