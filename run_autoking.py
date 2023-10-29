import sys
from AutoKing import AutoKing
import os

if __name__ == "__main__":
    if "-page" in sys.argv and "True" in sys.argv:
        path_to_streamlit_app = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/App.py"
        os.system(f'streamlit run {path_to_streamlit_app}')
    else:
        AutoKing()