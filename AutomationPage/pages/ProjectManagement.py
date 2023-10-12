import streamlit as st

feature_path = ""
bug_path = ""

def main():

    featureCol, bugCol = st.columns(2)
    with featureCol: st.write("Features Map"); st.write(load(feature_path))
    with bugCol : st.write("Bugs Map"); st.write(load(bug_path))

def load(path):
    return ["Feature1", "Feature2", "Feature3"]

def save(path, object):
    return None