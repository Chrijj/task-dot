# basic task list script
# currently python 2.7
# revision 0.8

from datetime import date
#import pickle
#import os

print
print '*' * 15
print "Task List Manager"
print '*' * 15

#test if file exists, if so import data
# if os.path.isfile("myfile.pkl"):
# 	try:
# 		pkl_file = open('myfile.pkl', 'rb')
# 		tasks = pickle.load(pkl_file) 
# 		pkl_file.close()
# 	except OSError:
# 		print "File Problem"
# else:
# 	tasks = {}

user_input = ""


class tasks(object):
	def __init__(self, name):
		self.name = name
		self.task_list = {}

	def listTasks(self):
		if self.task_list:
			for task, date in self.task_list.items():
				print "\t", task, ":", date
		else:
			print "No tasks currently in list"

	def addTask(self, task):
		if task not in self.task_list:
			self.task_list[task] = date.today()
			print task, "has been added to the task list"
		else:
			print task, "is already in the task list"

	def removeTask(self, task):
		if task in self.task_list:
			del self.task_list[task]
			print task, "has been removed from the task list"
		else:
			print task, "is not in the task list"

	# def __str__(self):
	# 	if self.task_list:
	# 		sorted_tasks = self.task_list.items()
	# 		sorted_tasks.sort()
	# 		printed_tasks = []
	# 		for task, date in sorted_tasks:
	# 			printed_tasks.append(task)
	# 			printed_tasks.append(":")
	# 			printed_tasks.append(date)
	# 			printed_tasks.append("\n")
	# 		return ''.join(printed_tasks)
	# 	else:
	# 		return "No Tasks currently in list"


tasks = tasks("taskList")

def script_response(user_input):
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks.addTask(user_input)
	elif user_input == 'd':
		user_input = raw_input("Enter the task: ")
		tasks.removeTask(user_input)
	elif user_input == 'l':
		tasks.listTasks()
	elif user_input == 'e':
		exit

while user_input != 'e':
	print
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, n' to add new, 'd' to delete or 'e' to exit\n.:")
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


