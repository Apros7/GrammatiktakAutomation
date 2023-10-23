import select
import pickle
import sys
import os
from datetime import datetime
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from usage_analytics import usage_script
from backup_data import backup_script
from backend_complexity import backend_complexity_script
from utils import divider, tiny_divider, countdown_timer

scripts = [
    usage_script,
    backup_script,
    backend_complexity_script
]

def user_input_timeout(prompt, timeout):
    print(prompt)
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist: return input()
    else: return None

class AutoKing():
    def __init__(self) -> None:
        print("\nI am AutoKing 👑, and I run Automation here.\nLet me see what needs to be done 👊\n")
        divider()
        print("Here is an overview of the scripts I am going to run: ")
        self.data = self.load_data()
        self.get_scripts_to_run()
        self.run_scripts()
        self.save_data()
        self.post_script_actions()

    def get_scripts_to_run(self) -> None:
        self.scripts_to_run = []
        tiny_divider()
        for script in scripts:
            last_date = "" if script.__str__ not in self.data else self.data[script.__str__]
            if not script.should_run(last_date): continue
            self.scripts_to_run.append(script)
        countdown_timer(5)
    
    def run_scripts(self) -> None:
        for script in self.scripts_to_run: 
            print(f"Running {script.__str__}:"); tiny_divider(); script_success = script.run(); 
            if script_success: self.data[script.__str__] = datetime.now(); 
            divider()

    def post_script_actions(self):
        print("I am now done with all scripts :-).")
        tiny_divider()
        path_to_streamlit_app = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutomationPage/App.py"
        print(f"To view the report use: 'streamlit run {path_to_streamlit_app}'")
        if user_input_timeout("Press enter to run this command or wait 5 seconds...", 5) is not None:
            print("Starting usage analytics frontend")
            os.system(f'streamlit run {path_to_streamlit_app}')
        divider()

    def load_data(self):
        data = pickle.load(open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutoKing/script_run_dates.pickle", "rb"))
        return data

    def save_data(self):
        with open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutoKing/script_run_dates.pickle", "wb") as file:
            pickle.dump(self.data, file)
        print("Script dates updated.")