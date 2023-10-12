import sys
import os
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from usage_analytics.firestore_client import FirestoreClient
from utils import Script

def get_report():
    print("Getting Firestore Objects: ")
    FirestoreClient().update()
    print("Report is now ready to be viewed!")
    return True # script succeeded
    
usage_script = Script(3, "Usage Analytics Report", get_report)

if __name__ == "__main__": 
    os.system('streamlit run /Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/data_review/App.py')