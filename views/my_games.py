import streamlit as st 

st.title("The Games I am Playing")
st.write("I have played many games before but this is just a list of the ones I am currently playing.")

my_games = {
    "Destiny 2": "https://www.youtube.com/watch?v=dZrxWFrd1zQ",
    "Guild Wars 2": "https://www.youtube.com/watch?v=rkPwxUu6kSI",
    "Deep Rock Galactic": "https://youtu.be/k4m_5JYrAGM?si=gCV0mNxD7lpH4OuN",
    "PVZ: Garden Warfare 2": "https://youtu.be/9_0gZFfqK3w?si=TzmYtPCAjiqw1464",
}

select_video = st.selectbox("Watch the trailer of my favorite games!", list(my_games.keys()))

video = my_games[select_video]

st.video(video, autoplay=True)