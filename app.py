import streamlit as st
from src.preprocessing import load_data, create_user_movie_matrix
from src.model import CollaborativeFiltering, ContentBased
from src.recommend import recommend_user, recommend_movie

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")

# ✅ Cache data
@st.cache_data
def load_all():
    return load_data(
        "data/movies.csv",
        "data/ratings.csv",
        "data/links.csv"
    )

movies, ratings, links = load_all()

@st.cache_data
def get_matrix(ratings):
    return create_user_movie_matrix(ratings)

matrix = get_matrix(ratings)

# Models
cf = CollaborativeFiltering(matrix)
cf.compute_similarity()

cb = ContentBased(movies)
cb.compute_similarity()

mode = st.radio("Choose Mode:", ["User Based", "Movie Based"])

# 🔹 USER BASED
if mode == "User Based":
    user_id = st.number_input("Enter User ID", min_value=1, max_value=610)

    if st.button("Recommend"):
        results = recommend_user(user_id, matrix, cf, movies, links)

        cols = st.columns(5)
        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 5]:
                st.image(row['poster'])
                st.write(row['title'])
                st.caption(row['genres'])

# 🔹 MOVIE BASED
else:
    movie = st.selectbox("Select Movie", movies['title'].values)

    if st.button("Recommend Similar"):
        results = recommend_movie(movie, cb, movies, links)

        cols = st.columns(5)
        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 5]:
                st.image(row['poster'])
                st.write(row['title'])
                st.caption(row['genres'])