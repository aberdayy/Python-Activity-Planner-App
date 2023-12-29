import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from saveDefinedTask import save_to_csv
from exceptionHandler import  check_duplicate_date
import tkcalendar
from displayController import read_task_data

root = tkinter.Tk()
root.title("Task Manager")
root.geometry("500x500")


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
			day = start + datetime.timedelta(days=i)
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



#Beni de bu kod ile beraber topraga gomun
	def save_note():
		task_dates, task_description = get_task_details()
		try:
			check_duplicate_date(task_dates, 'task_data.csv')
			# If no exception is raised, proceed to add the task for this date
			print("no exception")
			save_to_csv(task_dates, task_description)
		except Exception as e:
			print("hata burada")
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

root.mainloop()
