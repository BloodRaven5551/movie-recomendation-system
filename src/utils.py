import requests

API_KEY="39276e2761db2a5dfca927607dd76ed3"

def fetch_poster(tmdb_id):
    if tmdb_id!=tmdb_id:
        return None

    url=f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?api_key={API_KEY}"

    try:
        response=requests.get(url)
        data=response.json()

        poster_path=data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        return None
    
    return None