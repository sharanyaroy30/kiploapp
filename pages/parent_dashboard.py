import streamlit as st
import pandas as pd

def run():
    st.header("Parent Dashboard")
    
    # Simulated data for activity progress
    activity_data = {
        "Kid": ["Kid 1", "Kid 2", "Kid 3"],
        "Activity": ["Story Builder", "Puzzle Zone", "Story Builder"],
        "Progress": ["80%", "60%", "90%"]
    }
    
    df = pd.DataFrame(activity_data)
    st.write("Here’s a summary of your child's progress in various activities:")
    st.dataframe(df)
    
    # Display parent feedback form
    st.subheader("Provide Feedback")
    feedback = st.text_area("Leave your feedback for the activity:")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.error("Please write some feedback before submitting.")

