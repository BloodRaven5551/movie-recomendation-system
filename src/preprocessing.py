import pandas as pd

def load_data(movies_path,ratings_path):
    movies=pd.read_csv(movies_path)
    ratings=pd.read_csv(ratings_path)
    return movies,ratings


def create_user_movie_matrix(ratings):
    user_movie_matrix=ratings.pivot_table(
        index='userId',
        columns='movieId',
        values='rating'
    )
    return user_movie_matrix


def merge_movie_data(movies,ratings):
    return pd.merge(ratings,movies,on='movieId')