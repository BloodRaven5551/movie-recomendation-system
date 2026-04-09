import pandas as pd
from src.utils import fetch_poster


def recommend_user(user_id, matrix, model, movies, links, n=5):
    users = model.get_similar_users(user_id)
    scores = {}

    for u in users:
        ratings = matrix.iloc[u]
        for m, r in ratings.items():
            if pd.isna(matrix.loc[user_id, m]) and not pd.isna(r):
                scores[m] = scores.get(m, 0) + r

    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]
    ids = [i[0] for i in top]

    result = movies[movies['movieId'].isin(ids)]
    result = pd.merge(result, links, on='movieId')
    result['poster'] = result['tmdbId'].apply(fetch_poster)

    return result[['title', 'genres', 'poster']]


def recommend_movie(title, cb_model, movies, links, n=5):
    recs = cb_model.recommend(title, n)
    recs = pd.merge(recs, links, on='movieId')
    recs['poster'] = recs['tmdbId'].apply(fetch_poster)

    return recs[['title', 'genres', 'poster']]