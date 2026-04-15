import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


class CollaborativeFiltering:
    def __init__(self, matrix):   
        self.matrix = matrix
        self.similarity = None

    def compute_similarity(self):
        self.similarity = cosine_similarity(self.matrix.fillna(0))

    def get_similar_users(self, user_id, top_n=10):
        scores = self.similarity[user_id - 1]
        return np.argsort(scores)[::-1][1:top_n+1]


class ContentBased:
    def __init__(self, movies):
        self.movies = movies
        self.similarity = None

    def compute_similarity(self):
        cv = CountVectorizer(stop_words='english')
        vectors = cv.fit_transform(self.movies['genres'])
        self.similarity = cosine_similarity(vectors)

    def recommend(self, title, n=10):
        idx = self.movies[self.movies['title'] == title].index[0]
        distances = list(enumerate(self.similarity[idx]))
        distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:n+1]
        indices = [i[0] for i in distances]
        return self.movies.iloc[indices]