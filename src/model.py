import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split


# -------------------- COLLABORATIVE FILTERING --------------------
class CollaborativeFiltering:
    def __init__(self, matrix):
        self.matrix = matrix
        self.similarity = None

    def compute_similarity(self):
        self.similarity = cosine_similarity(self.matrix.fillna(0))

    def get_similar_users(self, user_id, top_n=10):
        scores = self.similarity[user_id - 1]
        return np.argsort(scores)[::-1][1:top_n+1]


# -------------------- CONTENT BASED (TF-IDF UPDATED) --------------------
class ContentBased:
    def __init__(self, movies):
        self.movies = movies
        self.similarity = None

    def compute_similarity(self):
        tfidf = TfidfVectorizer(stop_words='english')
        vectors = tfidf.fit_transform(self.movies['genres'])

        self.similarity = cosine_similarity(vectors)

    def recommend(self, title, n=10):
        idx = self.movies[self.movies['title'] == title].index[0]
        distances = list(enumerate(self.similarity[idx]))

        distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:n+1]
        indices = [i[0] for i in distances]

        return self.movies.iloc[indices]


# -------------------- SVD MODEL (NEW) --------------------
class SVDRecommender:
    def __init__(self, ratings):
        self.ratings = ratings
        self.model = None

    def train(self):
        reader = Reader(rating_scale=(1, 5))

        data = Dataset.load_from_df(
            self.ratings[['userId', 'movieId', 'rating']],
            reader
        )

        trainset, _ = train_test_split(data, test_size=0.2)

        self.model = SVD()
        self.model.fit(trainset)

    def predict(self, user_id, movie_id):
        return self.model.predict(user_id, movie_id).est