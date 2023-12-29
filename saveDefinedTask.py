import csv
import datetime
import time

def save_to_csv(task_dates, task_description):
    datesList = []
#Allah belani versin python
    for date in task_dates:
        global normalDate

        #Tarihim ay gun yil formatina degistirilmesi
        normalDate = date.strftime('%m/%d/%Y')
        '''print(f"normalDate degiskeni = {type(normalDate)}")
        print(normalDate)
        #Tarihten / isaretinin kaldirilmasi
        cizgisizZaman = normalDate.replace('/', '')

        #Tarihin parcalara ayrilmasi
        ay = cizgisizZaman[:2]
        gun = cizgisizZaman[2:4]
        yil = cizgisizZaman[4:8]
        print(f"gun : {gun}, ay: {ay}, yil: {yil}")

        #Timestamp olusturulma islemi
        x = datetime.datetime(int(yil), int(ay), int(gun))
        print(f"X: degeri = {x}")
        ts = time.mktime(x.timetuple())
'''
        #Olusturulan Timestampin listeye eklenmesi
        datesList.append(normalDate)

    with open('task_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datesList, task_description])