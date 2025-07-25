import streamlit as st
import pandas as pd
import pickle
from difflib import get_close_matches

# ✅ Set page config before everything
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# ✅ Load data (cached for performance)
@st.cache_data
def load_data():
    new_data = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return new_data, similarity

new_data, similarity = load_data()

# ✅ Find closest matching movie title
def correct_title(input_title):
    matches = get_close_matches(input_title, new_data['title'].values, n=1, cutoff=0.6)
    return matches[0] if matches else None

# ✅ Recommend top 5 similar movies
def recommend(movie):
    movie = correct_title(movie)
    if not movie:
        return ["Movie not found."], None
    movie_index = new_data[new_data['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [new_data.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies, movie

# ✅ Inject custom CSS for background and style
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1581905764498-189e50b5ddc7?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-attachment: fixed;
        color: #000000;
    }
    .movie-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 12px 20px;
        margin: 10px 0;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 500;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .title-style {
        background-color: rgba(0, 0, 0, 0.5);
        padding: 16px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ UI Elements
st.markdown('<div class="title-style"><h1>🎥 Movie Recommendation System</h1><p>📽️ Discover movies similar to your favorites</p></div>', unsafe_allow_html=True)
st.markdown("Enter any movie name you like (e.g. *Inception*, *Avatar*, *Titanic*) and get 5 related suggestions instantly!")

movie_input = st.text_input("🎞️ Enter a movie name:")

if st.button("🍿 Recommend"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie title.")
    else:
        results, matched_title = recommend(movie_input)
        if results[0] == "Movie not found.":
            st.error("❌ Movie not found. Try again.")
        else:
            st.success(f"🎯 Top 5 matches for '{matched_title}':")
            for i, movie in enumerate(results, start=1):
                st.markdown(f'<div class="movie-box">✅ {i}. {movie}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Powered by Scikit-learn & Pandas")
