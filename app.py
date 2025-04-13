import streamlit as st
from pages import story_builder, puzzle_zone, parent_dashboard
from utils import ai_prompts

# Set up the app title and layout
st.set_page_config(page_title="Kiplo: Creative Collaboration for Kids", layout="wide")

# Home Page Banner
st.image("assets/background.jpg", use_column_width=True)
st.title("Welcome to Kiplo!")
st.markdown("""
Kiplo is a creative platform designed to empower neurodivergent kids to engage in meaningful activities.
We provide a space for self-expression, creativity, and fun!
""")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose an activity:", ["Home", "Story Builder", "Puzzle Zone", "Parent Dashboard"])

# Routing to different pages
if page == "Home":
    st.write("Welcome to Kiplo! Choose an activity from the sidebar to get started.")
elif page == "Story Builder":
    story_builder.run()
elif page == "Puzzle Zone":
    puzzle_zone.run()
elif page == "Parent Dashboard":
    parent_dashboard.run()


