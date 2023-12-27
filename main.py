import datetime
import time
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2023, month = 12,
			day = 27)

cal.pack(pady = 20)

def getCalenderDate():
	gelenDate = cal.get_date()
	cizgisizZaman = gelenDate.replace('/','')
	ay = cizgisizZaman[:2]
	gun = cizgisizZaman[2:4]
	a = cizgisizZaman[4:6]
	str(a)
	yil = "20" + a
	x = datetime.datetime(int(yil), int(ay), int(gun))
	ts = time.mktime(x.timetuple())

	date.config(text = "Selected timestamp is: " + str(ts) + "\n Selected Date is: " + str(gelenDate))

# Add Button and Label
Button(root, text = "Get Date",command = getCalenderDate).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()
