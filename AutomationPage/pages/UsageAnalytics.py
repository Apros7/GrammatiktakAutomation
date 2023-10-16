import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime, timedelta
from matplotlib.ticker import MaxNLocator
import numpy as np
import re

def main():
    st.header("All text processed on the backend:")

    with open("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics/datastore/Backend-alltext.json", "r") as json_file:
        alltext = json.load(json_file)

    df_alltext = pd.DataFrame(alltext)
    df_alltext.drop_duplicates(subset='text', inplace=True)
    target_strings = ["Hej, jeg hedder Lucas.", "hvad hedder du", "jeg er sej", "jeg hedder benny", "hej jeg heder lucas"]

    fix = lambda x: re.sub(r'[^\w\s]', '', x.lower().replace(" ", ""))

    contains_target = df_alltext['text'].apply(lambda x: all([fix(target_string) not in fix(x) for target_string in target_strings]))
    partly_filtered_df = df_alltext[contains_target]
    contains_target_reverse = partly_filtered_df['text'].apply(lambda x: all([fix(x) not in fix(target_string) for target_string in target_strings]))
    filtered_df = partly_filtered_df[contains_target_reverse]
    st.dataframe(filtered_df)

    st.header("Usage Analytics")
    all_times = filtered_df["time"].to_list()
    counts = Counter([time[:10] for time in all_times if time != "unknown"])
    times = list(counts.keys())
    time_values = list(counts.values())

    values = [x for x in filtered_df["moduleTracking"].to_list() if len(x) > 0]

    sums = {}
    counts = {}

    for dictionary in values:
        for key, value in dictionary.items():
            if key not in sums: sums[key] = {"time": 0, "corrections": 0}
            sums[key]["time"] += value["time"]
            sums[key]["corrections"] += value["corrections"]
            counts[key] = counts.get(key, 0) + 1

    averages = {key: {"time": sums[key]["time"] / counts[key], "corrections": sums[key]["corrections"] / counts[key]} for key in sums}

    modules = [k.replace("Corrector", "").replace("Checker", "").replace("Spell", "Spelling") for k in averages.keys()]
    module_tracking_time = [v["time"] for v in averages.values()]
    module_tracking_corrections = [v["corrections"] for v in averages.values()]

    date_format = '%Y-%m-%d'
    times = [datetime.strptime(date, date_format) for date in times]

    min_date = min(times)
    max_date = max(times)

    all_dates = [min_date + timedelta(days=i) for i in range((max_date - min_date).days + 1)]
    all_dates = [date.strftime(date_format) for date in all_dates]

    expanded_times = all_dates
    expanded_values = [time_values[times.index(date)] if date in times else 0 for date in all_dates]

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(times, time_values)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.xticks(rotation=20)
        plt.xlabel('Date')
        plt.ylabel('Occurrences')
        plt.title("Occurrences over time")
        plt.tight_layout()

        st.pyplot(fig)

    with col2:

        # Maybe would be nice to be able to freeze current state when a big update is due and then be 
        # able to track from there an onwards to see the difference
        # some statistics about how many error messages are approved would also be extremely nice!!

        max_tracking_time = max(module_tracking_time)
        max_corrections = max(module_tracking_corrections)
        y_axis_buffer = 0.20 

        y_axis_upper_limit_tracking_time = max_tracking_time + max_tracking_time * y_axis_buffer
        y_axis_upper_limit_effectiveness = max_corrections + max_corrections * y_axis_buffer

        fig, ax1 = plt.subplots(figsize=(10, 6.2))

        bar_width = 0.35
        index = np.arange(len(modules))

        ax1.bar(index, module_tracking_time, bar_width, label='Time taken per word', color='b')
        ax1.set_xlabel('Module')
        ax1.set_ylabel('Time per word', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.set_xticks(index)
        ax1.set_xticklabels(modules, rotation = 20)
        ax1.set_title("Average time and corrections per word for each module")
        ax1.set_ylim([0, y_axis_upper_limit_tracking_time])

        ax2 = ax1.twinx()
        ax2.bar(index + bar_width, module_tracking_corrections, bar_width, label='No. Corrections per word', color='r', alpha=0.7)
        ax2.set_ylabel('Corrections per word', color='r')
        ax2.tick_params(axis='y', labelcolor='r')
        ax2.set_ylim([0, y_axis_upper_limit_effectiveness])
        ax2.set_xlim([-bar_width, len(modules) - bar_width])

        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        combined_handles = handles1 + handles2
        combined_labels = labels1 + labels2
        ax1.legend(combined_handles, combined_labels, loc='upper right', frameon=False) # one single legend

        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.show()

        st.pyplot(fig)

main()