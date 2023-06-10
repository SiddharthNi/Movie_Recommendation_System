

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{'
                '}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data= response.json()
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How Would You Like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    recommended_movies,recommended_movie_posters= recommend(selected_movie_name)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
     st.text(recommended_movies[0])
     st.image(recommended_movie_posters[0])
with col2:
     st.text(recommended_movies[1])
     st.image(recommended_movie_posters[1])
with col3:
    st.text(recommended_movies[2])
    st.image(recommended_movie_posters[2])
with col4:
    st.text(recommended_movies[3])
    st.image(recommended_movie_posters[3])
with col5:
    st.text(recommended_movies[4])
    st.image(recommended_movie_posters[4])

