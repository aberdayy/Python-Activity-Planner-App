import csv

def read_task_data():
    with open('task_data.csv', mode='r') as file:
        task_data = []
        reader = csv.reader(file)
        for row in reader:
            task_data.append(row)
    return task_data
