import streamlit as st
from src.preprocessing import load_data, create_user_movie_matrix
from src.model import CollaborativeFiltering, ContentBased
from src.recommend import recommend_user, recommend_movie

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("""
<style>
.movie-card {
    background-color: #1c1f26;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    transition: transform 0.2s ease;
}
.movie-card:hover {
    transform: translateY(-5px);
}
.movie-title {
    font-size: 14px;
    font-weight: 600;
    margin-top: 8px;
}
.movie-genre {
    font-size: 12px;
    color: #9aa0a6;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommendation System")


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


cf = CollaborativeFiltering(matrix)
cf.compute_similarity()

cb = ContentBased(movies)
cb.compute_similarity()


search = st.text_input("🔍 Search movie (for movie-based recommendations)")

mode = st.radio("Choose Mode:", ["Movie Based", "User Based"])

def show_movies(results):
    cols = st.columns(5)
    for i, (_, row) in enumerate(results.iterrows()):
        with cols[i % 5]:
            st.markdown('<div class="movie-card">', unsafe_allow_html=True)
            if row['poster']:
                st.image(row['poster'], use_container_width=True)
            st.markdown(f"<div class='movie-title'>{row['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='movie-genre'>{row['genres']}</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


if mode == "Movie Based":
    movie_list = movies['title'].values

    if search:
        movie_list = [m for m in movie_list if search.lower() in m.lower()]

    selected_movie = st.selectbox("Select Movie", movie_list)

    if st.button("Recommend Similar"):
        results = recommend_movie(selected_movie, cb, movies, links)
        show_movies(results)

else:
    user_id = st.number_input("Enter User ID", min_value=1, max_value=610)

    if st.button("Recommend for User"):
        results = recommend_user(user_id, matrix, cf, movies, links)
        show_movies(results)