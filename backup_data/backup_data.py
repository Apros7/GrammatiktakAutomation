##
# This file should save all relevant dataset to backup system (usb)
# every sunday
##

import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from utils import Script

def backup_data():
    print("Backing up data")

backup_script = Script(3, "Backup Data", backup_data)