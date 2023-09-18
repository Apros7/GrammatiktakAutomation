import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from usage_analytics.usage_analytics_report import usage_script
from backup_data.backup_data import backup_script
from utils import divider, tiny_divider, countdown_timer

scripts = [
    usage_script,
    backup_script
]

class AutoKing():
    def __init__(self) -> None:
        print("I am AutoKing 👑, and I run Automation here.\nLet me see what needs to be done 👊\n")
        divider()
        print("Here is an overview of the scripts I am going to run: ")
        self.get_scripts_to_run()
        self.run_scripts()

    def get_scripts_to_run(self) -> None:
        self.scripts_to_run = []
        tiny_divider()
        for script in scripts:
            if not script.should_run(): print(f"❌ {script.__str__}"); continue
            print(f"✅ {script.__str__}")
            self.scripts_to_run.append(script)
        countdown_timer(5)
    
    def run_scripts(self) -> None:
        for script in self.scripts_to_run: print(f"Running {script.__str__}:"); tiny_divider(); script.run(); divider()