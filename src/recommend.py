import pandas as pd
from src.utils import fetch_poster


def recommend_movies(user_id, user_movie_matrix, model, movies, links, num_recommendations=5):

    similar_users = model.get_similar_users(user_id)

    recommended_movies = {}

    for sim_user in similar_users:
        user_ratings = user_movie_matrix.iloc[sim_user]

        for movie_id, rating in user_ratings.items():
            if pd.isna(user_movie_matrix.loc[user_id, movie_id]) and not pd.isna(rating):
                recommended_movies[movie_id] = recommended_movies.get(movie_id, 0) + rating

    recommended_sorted = sorted(
        recommended_movies.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top_movies = [movie_id for movie_id, _ in recommended_sorted[:num_recommendations]]

    result = movies[movies['movieId'].isin(top_movies)]
    result = pd.merge(result, links, on='movieId')

    # Add poster URLs
    result['poster'] = result['tmdbId'].apply(fetch_poster)

    return result[['title', 'genres', 'poster']]