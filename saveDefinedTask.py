import csv
import datetime
import time

def save_to_csv(task_dates, task_description):
    datesList = []

    for date in task_dates:
        global normalDate

        normalDate = date.strftime('%m/%d/%Y')
        cizgisizZaman = normalDate.replace('/', '')
        ay = cizgisizZaman[:2]
        gun = cizgisizZaman[2:4]
        yil = cizgisizZaman[4:8]
        x = datetime.datetime(int(yil), int(ay), int(gun))
        ts = time.mktime(x.timetuple())
        datesList.append(int(ts))

    with open('task_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datesList, task_description])