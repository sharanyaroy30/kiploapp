import streamlit as st
from utils import ai_prompts, save_results
import random

def run():
    st.header("Story Builder")
    
    # Display a random AI-generated prompt
    prompt = ai_prompts.get_story_prompt()
    st.subheader("AI Story Prompt:")
    st.write(prompt)
    
    # Collect user input for the story
    character = st.text_input("Enter a character name:")
    setting = st.text_input("Where does the story take place?")
    plot = st.text_area("Describe the plot:")
    
    if st.button("Create Story"):
        if character and setting and plot:
            # Save the results to a CSV file for tracking progress
            save_results.save_story(character, setting, plot)
            st.success("Your story has been saved!")
        else:
            st.error("Please fill in all fields.")
    
    # Display the generated story
    if character and setting and plot:
        st.subheader("Your Story:")
        st.write(f"**Character:** {character}")
        st.write(f"**Setting:** {setting}")
        st.write(f"**Plot:** {plot}")
    else:
        st.write("Complete the form above to generate your story!")

