import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatikTAK/BackendAssistants/")
import streamlit as st

st.set_page_config(
    layout="wide",
    # initial_sidebar_state="collapsed"
)

st.header("Data Review Site")
st.write("Select the appropriate page to see more info on each statistic.")

import streamlit as st

# Create a dictionary to map page names to the corresponding module
# pages = {
#     "Feedback Overview": FeedbackOverview,
#     "Finance Report": FinanceReport,
#     "Project Management": ProjectManagement,
#     "Usage Analytics": UsageAnalytics,
# }

pages = {
    "Feedback Overview",
    "Finance Report",
    "Project Management",
    "Usage Analytics",
}

# columns = st.columns(4)
# for i, page in enumerate(pages):
#     with columns[i]:
#         button = st.button(page)
#     if button: st.experimental_set_query_params(page=i + 1); st.experimental_rerun()
    # if button: pages[page].main()