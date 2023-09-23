import pickle
import sys
from datetime import datetime
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from usage_analytics.usage_analytics_report import usage_script
from backup_data.backup_data import backup_script
from backend_complexity.backend_complexity import backend_complexity_script
from utils import divider, tiny_divider, countdown_timer

scripts = [
    usage_script,
    backup_script,
    backend_complexity_script
]

class AutoKing():
    def __init__(self) -> None:
        print("I am AutoKing 👑, and I run Automation here.\nLet me see what needs to be done 👊\n")
        divider()
        print("Here is an overview of the scripts I am going to run: ")
        self.data = self.load_data()
        self.get_scripts_to_run()
        self.run_scripts()
        self.save_data()

    def get_scripts_to_run(self) -> None:
        self.scripts_to_run = []
        to_print = []
        tiny_divider()
        for script in scripts:
            last_date = "" if script.__str__ not in self.data else self.data[script.__str__]
            if not script.should_run(last_date): to_print.append(f"❌ {script.__str__}"); continue
            print(f"✅ {script.__str__}")
            self.scripts_to_run.append(script)
        print(*to_print, sep="\n")
        countdown_timer(5)
    
    def run_scripts(self) -> None:
        for script in self.scripts_to_run: 
            print(f"Running {script.__str__}:"); tiny_divider(); script.run(); self.data[script.__str__] = datetime.now(); divider()

    def load_data(self):
        data = pickle.load(open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutoKing/script_run_dates.pickle", "rb"))
        return data

    def save_data(self):
        with open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/AutoKing/script_run_dates.pickle", "wb") as file:
            pickle.dump(self.data, file)