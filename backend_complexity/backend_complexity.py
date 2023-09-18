import os
import matplotlib.pyplot as plt
import pickle
import datetime

import sys
sys.path.append("/Users/lucasvilsen/Desktop/GrammatiktakAutomation")

from utils import Script

def count_lines_in_directory(directory):
    line_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    line_count += sum(1 for _ in f)
    return line_count

def make_plot():
    data = load_and_save_data()
    print("Plotting...")
    items = sorted([(str(k), v) for k, v in data.items()])
    dates = [k for k, v in items]
    values = [v for k, v in items]

    plt.figure(figsize=(10, 5))
    plt.bar(dates, values, width=0.5, color='skyblue', alpha=0.7)
    plt.title('Development of backend complexity (line count)')
    plt.xlabel('Date')
    plt.ylabel('Line count')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def load_and_save_data():
    print("Retrieving and saving data...")
    directory_path = "/Users/lucasvilsen/Desktop/GrammatikTAK/GrammatiktakBackend"
    path = "/Users/lucasvilsen/Desktop/GrammatiktakAutomation/backend_complexity/backend_complexity_over_time.pickle"
    data = pickle.load(open(path, "rb"))
    data["2023-09-01"] = 1648
    data[datetime.datetime.now().date()] = count_lines_in_directory(directory_path)
    with open(path, "wb") as file:
        pickle.dump(data, file)
    return data

backend_complexity_script = Script("Monday", "Backend_Complexity", make_plot)