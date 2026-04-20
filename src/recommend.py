import pandas as pd
from src.utils import fetch_poster


def recommend_user(user_id, matrix, model, movies, links, n=10):
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

    return result[['movieId', 'title', 'genres', 'poster']]


def recommend_movie(title, cb_model, movies, links, n=10):
    recs = cb_model.recommend(title, n)
    recs = pd.merge(recs, links, on='movieId')
    recs['poster'] = recs['tmdbId'].apply(fetch_poster)

    return recs[['title', 'genres', 'poster']]

def hybrid_score(cf_score, cb_score, svd_score,
                 w1=0.4, w2=0.3, w3=0.3):
    return (w1 * cf_score) + (w2 * cb_score) + (w3 * svd_score)