import streamlit as st 

st.title("Hobbies ", anchor=False)
st.write("Playing video games relieves some stress, so that's why I do it")

st.divider()

st.header("Game Profiles")
st.write("I mainly play games on steam")

st.subheader("Steam Profile")
st.image("images/steam_profile_logo.png", width=135)
st.link_button("Steemp", "https://steamcommunity.com/id/Steeemp/")

st.header("My Hobbies")
st.divider()

hobbies = [
    {
        "hobby" : "Playing Video Games",
        "image" : "images/gaming.jpg",
        "description" : "Reality sucks, video games is a way to immerse in a fantasy world, away from the troubles of the real world"
    },
    {
        "hobby" : "Drawing / Making Digital Art",
        "image" : "images/drawing.jpg",
        "description" : "Imagining wondeful things is not enough for me, I have to draw it."
    }
]

for i, hobby in enumerate(hobbies):
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(hobby['image'], width=250)
            
        with col2:
            st.header(hobby['hobby'])
            st.write(hobby['description'])
        
        st.divider()
