import pickle
import streamlit as st
import requests
import pandas as pd

st.markdown(
    """
    <style>
    /* Mengubah warna background halaman utama menjadi abu-abu gelap */
    .stApp {
        background-color: #2c2f33;
        color: white;
    }

    /* Menyembunyikan kotak di belakang teks select box */
    .stSelectbox label {
        background-color: #2c2f33 !important;
        color: white !important;
    }

    /* Mengubah warna box "choose an option" agar lebih terang */
    .stSelectbox div, .stSelectbox div div, .stSelectbox div div div {
        border-radius: 12px !important; /* Sudut tumpul */
        background-color: #23272a !important;
        border-color: #4f545c !important;
        color: white !important;
    }

    /* Mengubah warna box selectbox saat hover menjadi hitam */
    .stSelectbox div:hover, .stSelectbox div div:hover, .stSelectbox div div div:hover {
        background-color: #2c2f33;
        border-color: #23272a !important;
    }

    /* Mengubah warna tombol "Recommend" */
    .stButton > button {
        margin-top: 30px;
        background-color: #4f545c;
        color: white;
    }

    /* Mengubah warna tombol "Recommend" saat hover menjadi hitam */
    .stButton > button:hover {
        background-color: #23272a;
        color: white;
    }

    /* Menambahkan padding atas pada teks untuk mendekatkan dengan select box */
    .select-box-text {
        margin-top: 30px;
        margin-bottom: -20px; /* Atur margin bawah untuk mendekatkan */
    }
    
    .recommend-text {
        margin-top: 30px;
        margin-bottom: -30px; /* Atur margin bawah untuk mendekatkan */
    }
    
    .footer-text {
        font-size: 12px; /* Ukuran font kecil */
        color: #a9a9a9; /* Warna teks abu-abu */
        text-align: center; /* Rata tengah */
        margin-top: 200px; /* Margin atas */
        margin-bottom: -150px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=a6437a77b13974020f3220f6f9c30e6f&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('./model/movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('./model/similar.pkl','rb'))
st.title('🍿 CineCompass | Movie Recommender System')

st.markdown("<p class='select-box-text'>Pilih film favoritmu dari daftar di bawah ini:</p>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "",
    movies['title'].values,
    index=None 
)

st.markdown("<p class='recommend-text'>Click below for recomendation!</p>", unsafe_allow_html=True)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(names[i])
        col.image(posters[i])
        

# st.markdown("<p class='footer-text'>Made by Irgya Genta Arnezzi & Afzie Muhammad Nurlan</p>", unsafe_allow_html=True)