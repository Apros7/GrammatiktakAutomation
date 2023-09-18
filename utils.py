import datetime
import sys
import time

class Script:
    def __init__(self, day_to_run, purpose, script_to_run) -> None:
        self.__str__ = purpose
        self.check_day_to_run(day_to_run)
        self.script = script_to_run
        pass

    def check_day_to_run(self, day_to_run):
        to_number = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6, "eve": 7}
        if day_to_run.lower()[:3] not in to_number:
            raise ValueError(f"{day_to_run.lower()[:3]} not in {to_number.keys()}")
        self.day = to_number[day_to_run.lower()[:3]]

    def should_run(self):
        current_weekday = datetime.datetime.now().weekday()
        if current_weekday == self.day or self.day == 7: return True
        return False

    def run(self):
        self.script()

def divider(): print(f"{'=' * 40}")
def tiny_divider(): print(f"{'-' * 40}")

def countdown_timer(seconds):
    #Turns into a divider after 'seconds' seconds
    for i in range(seconds, -1, -1):
        if i == 0:
            sys.stdout.write("\r" + '=' * 40 + "\n")
        else:
            sys.stdout.write(f"\rRunning scripts in: {i}")
        sys.stdout.flush()
        time.sleep(1)
