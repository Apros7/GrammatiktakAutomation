import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatikTAK/BackendAssistants/")
import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.header("Data Review Site")
st.write("Select the appropriate page to see more info on each statistic.")

import streamlit as st
from pages import FeedbackOverview, FinanceReport, ProjectManagement, UsageAnalytics

# Create a dictionary to map page names to the corresponding module
pages = {
    "Project Management": ProjectManagement,
    "Finance Report": FinanceReport,
    "Usage Analytics": UsageAnalytics,
    "Feedback Overview": FeedbackOverview,
}

columns = st.columns(4)
for i, page in enumerate(pages):
    with columns[i]:
        button = st.button(page)
    if button: pages[page].main()