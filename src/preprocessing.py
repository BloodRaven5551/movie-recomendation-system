import pandas as pd

def load_data(movies_path, ratings_path, links_path):
    movies = pd.read_csv(movies_path)
    ratings = pd.read_csv(ratings_path)
    links = pd.read_csv(links_path)
    return movies, ratings, links


def create_user_movie_matrix(ratings):
    return ratings.pivot_table(
        index='userId',
        columns='movieId',
        values='rating'
    )