import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class CollaborativeFiltering:
    def __init__(self,user_movie_matrix):
        self.user_movie_matrix=user_movie_matrix
        self.user_similarity=None

    def compute_similarity(self):
        self.user_similarity=cosine_similarity(
            self.user_movie_matrix.fillna(0)
        )
        return self.user_similarity

    def get_similar_users(self,user_id,top_n=10):
        sim_scores=self.user_similarity[user_id-1]
        similar_users=np.argsort(sim_scores)[::-1][1:top_n+1]
        return similar_users