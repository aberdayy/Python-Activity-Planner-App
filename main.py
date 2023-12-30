from datetime import datetime, timedelta
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from saveDefinedTask import save_to_csv
from exceptionHandler import check_duplicate_date
import tkcalendar
from displayController import read_task_data
import csv

root = tkinter.Tk()
root.title("Task Manager")
root.geometry("500x500")


# Function to convert string dates to datetime objects
def parse_date(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y')


def display_tasks(tasks):
    new_window = tkinter.Toplevel(root)
    new_window.title("Task Display")

    tree = tkinter.ttk.Treeview(new_window)
    tree['columns'] = ('Start Date', 'End Date', 'Task')
    tree.heading('#0', text='Date')
    tree.heading('Start Date', text='Start Date')
    tree.heading('End Date', text='End Date')
    tree.heading('Task', text='Task')

    for date, tasks_list in tasks.items():
        for task in tasks_list:
            tree.insert('', 'end', text=date.strftime('%m/%d/%Y'), values=task)

    tree.pack(expand=True, fill='both')


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


# Callback functions for button clicks
def show_daily():
    tasks = read_task_data()  # Fetch tasks from CSV
    daily_tasks, _, _ = process_csv('task_data.csv')
    display_tasks(daily_tasks)


def show_weekly():
    tasks = read_task_data()  # Fetch tasks from CSV
    _, weekly_tasks, _ = process_csv('task_data.csv')
    display_tasks(weekly_tasks)


def show_biweekly():
    tasks = read_task_data()  # Fetch tasks from CSV
    _, _,_, biweekly_tasks = process_csv('task_data.csv')
    display_tasks(biweekly_tasks)


def display():
    tasks = read_task_data()  # Fetch tasks from CSV
    new_window = Toplevel(root)  # Create a new window
    new_window.title("Task Display")  # Set the title of the new window

    # Creating a Tkinter listbox to display tasks in the new window
    listbox = tkinter.Listbox(new_window, width=100, height=20)
    listbox.pack(padx=20, pady=20)

    # Inserting each task into the listbox
    for task in tasks:
        listbox.insert(tkinter.END, f"Dates: {task}")


'''datetime.fromtimestamp()
'''


def add_task():
    newWindow = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Add Task ")

    # sets the geometry of toplevel
    newWindow.geometry("500x500")

    def date_range(start, stop):
        dates = []
        diff = (stop - start).days
        for i in range(diff + 1):
            day = start + timedelta(days=i)
            dates.append(day)
        if dates:
            return dates
        else:
            messagebox.showinfo("error", "Make sure the end date is later than start date")
            print('Make sure the end date is later than start date')
            return None

    def get_task_details():
        task_dates = date_range(date1.get_date(), date2.get_date())
        task_description = entry.get()
        return task_dates, task_description

    # Beni de bu kod ile beraber topraga gomun
    def save_note():
        task_dates, task_description = get_task_details()
        string_date = []
        for date in task_dates:
            x = date.strftime('%m/%d/%Y')
            string_date.append(x)
        try:
            check_duplicate_date(string_date, 'task_data.csv')
            # If no exception is raised, proceed to add the task for this date
            save_to_csv(string_date, task_description)
            messagebox.showinfo("Succesfull", "Your task is succcesfully saved! You can now close these windows.")
        except Exception as e:
            messagebox.showinfo("Error Creating Note", f"Warning! => {e}")

    # Print the exception message if a duplicate date is found
    startDate = Label(newWindow, text="Task Start Date : ").place(x=60, y=10)
    endDate = Label(newWindow, text="Task End Date : ").place(x=60, y=50)

    date1 = tkcalendar.DateEntry(newWindow)
    date1.pack(padx=10, pady=10)
    date2 = tkcalendar.DateEntry(newWindow)
    date2.pack(padx=10, pady=10)

    Button(newWindow, text='Save Task Dates', command=lambda: date_range(date1.get_date(), date2.get_date())).pack()

    label = Label(newWindow, text="Task Description:").pack()

    entry = Entry(newWindow, width=40)
    entry.focus_set()
    entry.pack()

    Button(newWindow, text="Save Description", width=20).pack(pady=20)

    Button(newWindow, text="Save note", width=50, command=save_note).pack(pady=50)


add_task_button = tkinter.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=20)

display_tasks_button = tkinter.Button(root, text="Display Tasks", command=display)
display_tasks_button.pack(pady=20)

daily_button = tkinter.Button(root, text="Show Daily Tasks", command=show_daily)
daily_button.pack()

weekly_button = tkinter.Button(root, text="Show Weekly Tasks", command=show_weekly)
weekly_button.pack()

biweekly_button = tkinter.Button(root, text="Show Bi-Weekly Tasks", command=show_biweekly)
biweekly_button.pack()

root.mainloop()
