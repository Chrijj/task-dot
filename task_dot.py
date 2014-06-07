# basic task list script
# python 2.7
# revision a1.1

from datetime import date
import cPickle as pickle
import os

print
print '*' * 15
print "Task List Manager"
print '*' * 15

class tasks(object):
	def __init__(self, name):
		self.name = name
		self.task_list = {}

	def listTasks(self):
		if self.task_list:
			for task, date in self.task_list.items():
				print "\t", task, ":", date
		else:
			print "\t No tasks currently in list"

	def addTask(self, task):
		if task not in self.task_list:
			self.task_list[task] = date.today()
			print "\t", task, "has been added to the task list"
		else:
			print "\t", task, "is already in the task list"

	def removeTask(self, task):
		if task in self.task_list:
			del self.task_list[task]
			print "\t", task, "has been removed from the task list"
		else:
			print "\t", task, "is not in the task list"

	def __str__(self):
		return self.name + " : " + str(len(self.task_list)) + " items"
		

#test if file exists, if so import data
if os.path.isfile("task_data.pkl"):
	try:
		pkl_in = open('task_data.pkl', 'rb')
		my_tasks = pickle.load(pkl_in) 
		pkl_in.close()
	except OSError:
		print "Problem loading from file"
else:
	my_tasks = tasks("Basic List")


def script_response(user_input):
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		my_tasks.addTask(user_input)
	elif user_input == 'd':
		user_input = raw_input("Enter the task: ")
		my_tasks.removeTask(user_input)
	elif user_input == 'l':
		my_tasks.listTasks()
	elif user_input == 'p':
		print my_tasks
	elif user_input == 'e':
		pkl_out = open('task_data.pkl', 'wb')
		pickle.dump(my_tasks, pkl_out)
		pkl_out.close()	
		exit

user_input = ""

while user_input != 'e':
	print
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, 'p' for a summary, 'n' to add new, 'd' to delete or 'e' to exit\n.:")
	script_response(user_input)


# def script_response(user_input):
# 	"""takes in a string used to determine a control flow
# 		of output responses"""
# 	if user_input == 'n':
# 		user_input = raw_input("Enter the task: ")
# 		tasks[user_input] = date.today()
# 		print "\t Task", user_input, "added to task list"
# 	elif user_input == 'd':
# 		if tasks:
# 			sorted = tasks.items()
# 			sorted.sort()
# 			for key, value in sorted:
# 				print "\t", value, key
# 			user_input = raw_input("\nTask to delete: ")
# 			if user_input not in tasks:
# 				print "\t That task does not exist."
# 			else:
# 				del tasks[user_input]
# 				print "\t", user_input, "removed from tasks."
# 		else:
# 			print "\t No Tasks in list"
# 	elif user_input == 'l':
# 		if tasks:
# 			sorted = tasks.items()
# 			sorted.sort()
# 			for key, value in sorted:
# 				print "\t", value, key
# 		else:
# 			print "\t No Tasks in list"
# 	elif user_input == 'e':
# 		output = open('myfile.pkl', 'wb')
# 		pickle.dump(tasks, output)
# 		output.close()
# 		exit
# 	else:
# 		print "\t Invalid input, try again"


