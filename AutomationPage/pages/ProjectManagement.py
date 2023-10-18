import streamlit as st

projects_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/projects.csv"
feature_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/features.csv"
bug_path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/pages/data/projects/bugs.csv"

# functions
def view_project(project):
    featureCol, bugCol = st.columns(2)
    with featureCol: st.write("Features Map"); display(feature_path, project)
    with bugCol : st.write("Bugs Map"); display(bug_path, project)

def display(path, project):
    project_index = project.split(":")[0]
    project_dict = sort(load(path))
    st.write(project_dict[project_index])

def sort(values):
    project_dict = {}
    for v in values:
        v, k = v.split(",")
        if k in project_dict: project_dict[k].append(v)
        else: project_dict[k] = [v]
    return project_dict

def load(path):
    return open(path, "r").read().splitlines()

def save(path, object):
    return None

def add_buttons():
    col1, col2, col3, col4 = st.columns(4)
    with col1: type_to_add = st.selectbox("Project, feature or bug?", ["Project", "Feature", "Bug"])
    with col2: name = st.text_input("Name: ")
    with col3: hours = st.number_input("Estimated time to completion (hours)?")
    with col4: st.write(""); st.write(""); submit = st.button("Submit")
    if type_to_add != "Project": 
        associated_project, how_critical = add_extra_buttons(col1, col2, col3)
    if submit: add_project(type_to_add, name, hours, associated_project, how_critical)

def add_extra_buttons(col1, col2, col3):
    projects = load(projects_path)
    with col1: associated_project = st.selectbox("Associated project?", projects)
    with col2: how_critical = st.selectbox("How critical is this to get done?", ["Low", "Medium", "High", "Extremely Critical"])
    return associated_project, how_critical

def add_project(type_to_add, name, hours, associated_project, how_critical):
    pass

def register_time():
    pass

# script: 
def main():
    projects = load(projects_path)

    st.title("Choose project:")
    project = st.selectbox("Avaliable projects", projects)
    view_project(project)

    st.divider()
    st.title("Add project, feature or bug")
    add_buttons()

    st.divider()
    st.title("Register time")
    register_time()

main()