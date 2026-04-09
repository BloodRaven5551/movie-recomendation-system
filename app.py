import streamlit as st
from src.preprocessing import load_data, create_user_movie_matrix
from src.model import CollaborativeFiltering
from src.recommend import recommend_movies

st.title("🎬 Movie Recommendation System")


movies, ratings, links = load_data(
    "data/movies.csv",
    "data/ratings.csv",
    "data/links.csv"
)

user_movie_matrix = create_user_movie_matrix(ratings)


model = CollaborativeFiltering(user_movie_matrix)
model.compute_similarity()


user_id = st.number_input("Enter User ID (1–610)", min_value=1, max_value=610)

if st.button("Get Recommendations"):

    results = recommend_movies(
        user_id,
        user_movie_matrix,
        model,
        movies,
        links
    )

    st.subheader("Recommended Movies:")

    for _, row in results.iterrows():
        st.write(f"### {row['title']}")
        st.write(row['genres'])

        if row['poster']:
            st.image(row['poster'], width=200)