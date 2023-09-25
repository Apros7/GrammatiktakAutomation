import datetime
import sys
import time

class Script:
    def __init__(self, days_between_runs, purpose, script_to_run) -> None:
        self.__str__ = purpose
        self.days_between_runs = days_between_runs
        self.script = script_to_run

    def should_run(self, last_run):
        if last_run == "": return True
        difference = datetime.datetime.now() - last_run
        if difference.days >= self.days_between_runs: print(f"✅ {self.__str__}"); return True
        distance = " " * (30 - len(self.__str__))
        print(f"❌ {self.__str__}{distance} - Running in {self.days_between_runs - difference.days} days")
        return False

    def run(self):
        self.script()

length_of_dividers = 60

def divider(): print(f"{'=' * length_of_dividers}")
def tiny_divider(): print(f"{'-' * length_of_dividers}")

def countdown_timer(seconds):
    #Turns into a divider after 'seconds' seconds
    for i in range(seconds, -1, -1):
        if i == 0:
            sys.stdout.write("\r" + '=' * length_of_dividers + "\n")
        else:
            sys.stdout.write(f"\rRunning scripts in: {i}")
        sys.stdout.flush()
        time.sleep(1)
