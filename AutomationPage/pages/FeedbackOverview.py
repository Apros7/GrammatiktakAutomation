import json
import streamlit as st
import pandas as pd


def main():
    st.header("Feedback sent to backend:")

    with open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/datastore/Feedback.json", "r") as json_file:
        feedback = json.load(json_file)

    df_feedback = pd.DataFrame(feedback)

    st.dataframe(df_feedback)