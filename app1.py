import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image


# def fetch_poster(music_id, k):
#     # response = requests.get('https://api.themusicdb.org/3/music/{}?api_key=461b48a5dd075f3266a1e812b31d5ee9'.format(music_id))
#     # poster = response.json()
#     if(k == 0) :
#         return 'C:\Users\hp\Desktop\mlproject\img\img1.jpg'
#     if(k == 1) :
#         return 'C:\Users\hp\Desktop\mlproject\img\img2.jpg'
#     if(k == 2) :
#         return 'C:\Users\hp\Desktop\mlproject\img\img3.jpg'
#     if(k == 3) :
#         return 'C:\Users\hp\Desktop\mlproject\img\img4.jpg'
#     return 'C:\Users\hp\Desktop\mlproject\img\img5.jpg'

    
    # return 'https://image.tmdb.org/t/p/w500/' + poster['poster_path']

def recommend(music1) :
    ind = music[music['track_name'] == music1].index[0]
    dis=sim[ind]
    recom_list = sorted(list(enumerate(dis)),reverse = True,key = lambda x : x[1])[1:6]
    recommended_music = []
    recommended_posters = []
    for i in recom_list:
        music_id=i[0]
        recommended_music.append(music.iloc[i[0]].track_name)
         # fetch poster from api
        # recommended_posters.append(fetch_poster(music_id,i))
    return recommended_music
music_dict= pickle.load(open('music_dict.pkl','rb'))
music=pd.DataFrame(music_dict)

sim=pickle.load(open('sim.pkl','rb'))
st.title('Music Recommender System')

selected_music_name = st.selectbox(
    'Which music would like to listen',
    music['track_name'].values
)
if st.button('Recommend'):
    names=recommend(selected_music_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        image = Image.open('img/img1.jpg')
        st.image(image)

    with col2:
        st.text(names[1])
        image = Image.open('img/img2.jpg')
        st.image(image)

    with col3:
        st.text(names[2])
        image = Image.open('img/img3.jpg')
        st.image(image)

    with col4:
        st.text(names[3])
        image = Image.open('img/img4.jpg')
        st.image(image)

    with col5:
        st.text(names[4])
        image = Image.open('img/img5.jpg')
        st.image(image)