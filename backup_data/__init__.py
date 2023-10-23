##
# This file should save all relevant datasets & models to backup system (usb)
##

import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

import os
import shutil
import psutil
from datetime import datetime

from utils import Script, paint

dataset_folder = "/path/to/source/folder"
model_folder = "/path/to/models"
usb_drive_path = "/media/your-username/usb-drive-label/"

def get_space_avaliable():
    usage = psutil.disk_usage(usb_drive_path)

    remaining_bytes = usage.free
    remaining_megabytes = remaining_bytes / (1024 * 1024)
    remaining_gigabytes = remaining_megabytes / 1024

    print(f"Remaining space on '{usb_drive_path}':")
    print(f"Megabytes: {remaining_megabytes:.2f} MB")
    print(f"Gigabytes: {remaining_gigabytes:.2f} GB")
    return remaining_megabytes

def get_space_required():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dataset_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    for dirpath, dirnames, filenames in os.walk(model_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024)

def backup_data():
    print("Backing up data")
    paint(["Failed: ", "No paths..."], ["r", "b"])

    return False

    current_date = datetime.now().strftime("%d_%m_%Y")

    space_avaliable = get_space_avaliable()
    space_required = get_space_required()

    if space_required > space_avaliable:
        print("You need to clean up usb drive: ")
        print(f"{space_avaliable = }")
        print(f"{space_required = }")
        return False
        
    if os.path.exists(usb_drive_path):
        try:
            # Use shutil.copytree to copy the entire folder and its contents to the USB drive
            shutil.copytree(dataset_folder, os.path.join(usb_drive_path, f"datasets-{current_date}"))
            print(f"Folder '{dataset_folder}' successfully copied to USB drive.")
            shutil.copytree(model_folder, os.path.join(usb_drive_path, f"models-{current_date}"))
            print(f"Folder '{model_folder}' successfully copied to USB drive.")
            return True # script succeeded
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("USB drive not found. Please connect a USB drive and try again.")

    return False # script failed

backup_script = Script(3, "Backup Data", backup_data)