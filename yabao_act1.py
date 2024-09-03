import streamlit as st 


#----PAGE SETUP-----
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/person:",
    default=True,
)

page_2 = st.Page(
    page="views/hobby.py",
    title="Hobby",
    icon=":material/videogame_asset:"
)

project_1 = st.Page(
    page="views/project_1.py",
    title="Project 1",
    icon=":material/laptop_chromebook:"
)

snow = st.Page(
    page="views/snow.py",
    title="Snow test",
    icon=":material/ac_unit:"
)

baloon = st.Page(
    page="views/baloons.py",
    title="Baloon test",
    icon=":material/ac_unit:"
)

my_games = st.Page(
    page="views/my_games.py",
    title="My Games",
    icon=":material/stadia_controller:"
)
#--- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, page_2])

#--- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page, page_2, my_games],
        "Components test": [ snow, baloon]
    }
)

st.logo("images/logo1.png")
st.sidebar.text("made by Gil Joshua Yabao")

#-- RUN NAVIGATION --
pg.run()