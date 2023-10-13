import streamlit as st

projects_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/projects.csv"
feature_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/features.csv"
bug_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/bugs.csv"

# functions
def view_project(project):
    featureCol, bugCol = st.columns(2)
    with featureCol: st.write("Features Map"); st.write(load(feature_path))
    with bugCol : st.write("Bugs Map"); st.write(load(bug_path))

def load(path):
    return open(path, "r").read().splitlines()

def save(path, object):
    return None

# script: 

projects = load(projects_path)

print(projects)

st.title("Choose project:")
project = st.selectbox("Avaliable projects", projects)
view_project(project)