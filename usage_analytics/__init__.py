import select
import sys
import os
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from usage_analytics.firestore_client import FirestoreClient
from utils import Script

def get_report():
    print("Getting Firestore Objects: ")
    FirestoreClient().update()
    print("Report is now ready to be viewed!")
    print("To view the report use: 'streamlit run /Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/data_review/App.py'")
    if user_input_timeout("Press enter to run this command or wait 5 seconds...", 5) is not None:
        print("Starting usage analytics frontend")
        os.system('streamlit run /Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/data_review/App.py')


def user_input_timeout(prompt, timeout):
    print(prompt)
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist: return input()
    else: return None
    
usage_script = Script(3, "Usage Analytics Report", get_report)

if __name__ == "__main__": 
    os.system('streamlit run /Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/data_review/App.py')