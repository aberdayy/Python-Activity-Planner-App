import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk

# Function to convert string dates to datetime objects
def parse_date(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y')

# Function to categorize dates into daily, weekly, or bi-weekly
def categorize_dates(dates):
    daily_data = {}
    weekly_data = {}
    biweekly_data = {}

    for start_date, end_date, task in dates:
        start = parse_date(start_date)
        end = parse_date(end_date)
        task_info = (start_date, end_date, task)

        # Daily
        while start <= end:
            if start not in daily_data:
                daily_data[start] = []
            daily_data[start].append(task_info)
            start += timedelta(days=1)

        # Weekly
        start = parse_date(start_date)
        while start <= end:
            week_start = start - timedelta(days=start.weekday())
            if week_start not in weekly_data:
                weekly_data[week_start] = []
            weekly_data[week_start].append(task_info)
            start += timedelta(weeks=1)

        # Bi-weekly
        start = parse_date(start_date)
        while start <= end:
            biweek_start = start - timedelta(days=start.weekday())
            if biweek_start not in biweekly_data:
                biweekly_data[biweek_start] = []
            biweekly_data[biweek_start].append(task_info)
            start += timedelta(weeks=2)

    return daily_data, weekly_data, biweekly_data

# Read CSV file and categorize dates
def process_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if exists
        date_data = [row[:3] for row in reader if len(row) >= 3 and all(row[:3])]

    daily, weekly, biweekly = categorize_dates(date_data)
    return daily, weekly, biweekly

# Create tkinter GUI to display the tasks based on the selected category
def display_tasks(tasks):
    root = tk.Tk()
    root.title("Task Display")

    tree = ttk.Treeview(root)
    tree['columns'] = ('Start Date', 'End Date', 'Task')
    tree.heading('#0', text='Date')
    tree.heading('Start Date', text='Start Date')
    tree.heading('End Date', text='End Date')
    tree.heading('Task', text='Task')

    for date, tasks_list in tasks.items():
        for task in tasks_list:
            tree.insert('', 'end', text=date.strftime('%m/%d/%Y'), values=task)

    tree.pack(expand=True, fill='both')
    root.mainloop()

# Callback functions for button clicks
def show_daily():
    display_tasks(daily_tasks)

def show_weekly():
    display_tasks(weekly_tasks)

def show_biweekly():
    display_tasks(biweekly_tasks)

# Sample CSV processing
csv_file_path = 'task_data.csv'  # Replace with your file path
daily_tasks, weekly_tasks, biweekly_tasks = process_csv(csv_file_path)

# Create tkinter window
root = tk.Tk()
root.title("Task Viewer")

# Buttons to display tasks
daily_button = tk.Button(root, text="Show Daily Tasks", command=show_daily)
daily_button.pack()

weekly_button = tk.Button(root, text="Show Weekly Tasks", command=show_weekly)
weekly_button.pack()

biweekly_button = tk.Button(root, text="Show Bi-Weekly Tasks", command=show_biweekly)
biweekly_button.pack()

root.mainloop()
