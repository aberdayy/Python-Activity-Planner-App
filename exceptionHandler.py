import csv
from datetime import datetime

from displayController import read_task_data
from saveDefinedTask import save_to_csv

'''def exceptionCheck(taskDates,description):
    tasks = read_task_data()  # Fetch tasks from CSV
    print("exception a geldik")
    for date in taskDates:
        if tasks[0] == date:
            print("Theres already task defined for those dates.")
        else:
            save_to_csv(taskDates,description)
            print("No exception")

'''
'''def check_duplicate_date(taskDates, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the date is in the first column of each row in the CSV file
#            for date in taskDates:
            #normalDate = date.strftime('%m/%d/%Y')

            print(f"Task Dates: {taskDates}")
            stored_date = row
            print(f"Stored Date: {stored_date[0]}")
            if stored_date[0] == taskDates:
                #raise Exception("There is already a task scheduled for this date.")
                 print("There is already a task scheduled for this date.")

    return False  # Return False if no duplicate dates are found

check_duplicate_date("['12/30/2023', '12/31/2023', '01/01/2024']",'task_data.csv')'''

def extract_date_int(date_list):
    return [int(date.split('/')[1]) for date in date_list]

def check_duplicate_date(task_dates, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        stored_dates = [row[0] for row in reader]  # Extract stored dates from the CSV file

    task_day_values = extract_date_int(task_dates)
    stored_day_values = extract_date_int(stored_dates)

    common_values = set(task_day_values).intersection(stored_day_values)

    if common_values:
        raise Exception("These dates are already has a task assigned!")
        return True  # Return True if there are common dates
    else:
        print("There are no common integer values in the lists.")
        return False  # Return False if there are no common dates

'''task_dates = ['12/30/2024', '12/31/2023', '01/01/2024']
csv_file = 'task_data.csv'
check_duplicate_date(task_dates, csv_file)'''