import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from utils import Script

def get_report():
    print("Here is my report:")

usage_script = Script("Sunday", "Usage Analytics Report", get_report)