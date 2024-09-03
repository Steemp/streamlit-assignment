import streamlit as st 

col1, col2 = st.columns(2)

def output_language_result(languages):
    for language, percentage in languages.items():
        st.write(f"{language}: {percentage}%")
        st.progress(percentage / 100)

with col1:
    st.title("Gil Joshua S. Yabao")
    st.write("An IT enthusiast studying in Cebu Institute of Technology University")
    st.text("Species: Human")
    st.text("Gender: Male")
    

with col2:
    st.image("images/profile.png")
    
st.title("Academic Projects")

academic_experiences = [
    {
        "school": "Cebu Institute of Technology - University",
        "date": "August 2024 - Present",
        "course": "Capstone and Research 2",
        "role": "Graphics Designer / UI/UX designer",
        "image": "images/cit_logo.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "January 2024 - May 2024",
        "course": "Capstone and Research 1",
        "image": "images/cit_logo.png",
        "role": "Backend Developer / Graphics Designer",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "August 2023 - December 2023",
        "course": "Industry Elective 1 & Applications Development and Emerging Technologies",
        "image": "images/cit_logo.png",
        "role": "Frontend Developer / Backend Developer / Graphics Designer",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words",
        "web_link": ""
    },
]

my_education = [
    {
        "school": "Cebu Institute of Technology - University",
        "level": "College",
        "address": "N. Bacalso Ave. Cebu City",
        "time": "2021 - Present",
        "image": "images/cit_logo.png"
        
    },{
        "school": "Cebu Institute of Technology - University",
        "level": "Grade 11 - 12",
        "address": "N. Bacalso Ave. Cebu City",
        "time": "2017 - 2019",
        "image": "images/cit_logo.png"
    },{
        "school": "St. Mary's Academy of San Nicolas",
        "level": "College",
        "address": "T. Abella Street. Cebu City",
        "time": "2013 - 2017",
        "image": "images/smasn.jpg"
    }
]

it_skills = {
    "Java" : 70,
    "C++" : 40,
    "Python" : 30,
    "Javascript": 45,
    "CSS (stylesheet language)": 65,
    "HTML (markup language)": 70
}

framework_exp ={
    "ReactJS": 75,
    "Springboot": 78
}
tab1, tab2, tab3 = st.tabs(["Projects", "Education", "Skills"])

with tab1:
    for i, experience in enumerate(academic_experiences):
        with st.expander(label=experience['course'], expanded=True):
            cols = st.columns([1, 4])

            with cols[0]:
                st.image(experience['image'], width=125)

            with cols[1]:
                st.markdown(f"**<span style='font-size:24px;'><a href=\"{experience['link']}\" style='text-decoration:none; color:#d33682;'>{experience['school']}</a></span>**", unsafe_allow_html=True)
                st.write(f" ##### {experience['course']}")
                st.write(f" ###### {experience['role']}")
                st.write(f"_{experience['date']}_")

                col1, col2, col3 = st.columns([3, 1, 1])

                with col1:
                    st.write(f"{experience['project']}")

                with col2:
                    st.link_button("Github", experience['github_link'], type="primary")

                # This one checks if web_link is None or "". That's the way I understood it and read it 

                if experience.get('web_link'):
                    with col3:   
                        st.link_button("Website", experience['web_link'], type="secondary")


        if i < len(academic_experiences) - 1:
            st.divider()
            
with tab2:
    for i, education in enumerate(my_education):
        with st.expander(label=education['level'], expanded=True):
            cols = st.columns([1, 4])

            with cols[0]:
                st.image(education['image'], width=125)

            with cols[1]:
                st.header(education['school'])
                st.subheader(education['address'])
                st.write(education['time'])
                
        if i < len(academic_experiences) - 1:
            st.divider()

with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Programming Language Experience")
        output_language_result(it_skills)
    with col2:
        st.subheader("Framework Experience")
        output_language_result(framework_exp)
    
    st.header("Other Skills")
    st.write("Digital Art")
    st.write("Animations")
    st.write("UI/UX Design")
        