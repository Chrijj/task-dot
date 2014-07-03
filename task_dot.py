# basic task list script
# python 2.7
# revision a1.2

from datetime import date
import cPickle as pickle
import os

class tasks(object):
	def __init__(self, name):
		self.name = name
		self.task_list = {}

	def listTasks(self):
		if self.task_list:
			for task, date in self.task_list.items():
				print "****", task, ":", date
		else:
			print "\t No tasks currently in list"

	def addTask(self, task):
		if task not in self.task_list:
			self.task_list[task] = date.today()
			print ">>> ", task, "has been added to the task list"
		else:
			print "xxx ", task, "is already in the task list"

	def removeTask(self, task):
		if task in self.task_list:
			del self.task_list[task]
			print "<<< ", task, "has been removed from the task list"
		else:
			print "xxx ", task, "is not in the task list"

	def __str__(self):
		return self.name + " : " + str(len(self.task_list)) + " items"
		

#import data from stored file
taskFile = "task_data.pkl"
try:
	pkl_in = open(taskFile, 'rb')
	my_tasks = pickle.load(pkl_in) 
	pkl_in.close()
	print "Task data loaded from file %s." % taskFile
except IOError:
	print "Problem loading from file %s." % taskFile
	my_tasks = tasks("Basic List")


def script_response(user_input):
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		my_tasks.addTask(user_input)
	elif user_input == 'd':
		my_tasks.listTasks()
		user_input = raw_input("Enter the task: ")
		my_tasks.removeTask(user_input)
	elif user_input == 'l':
		my_tasks.listTasks()
	elif user_input == 's':
		print my_tasks
	elif user_input == 'e':
		pkl_out = open('task_data.pkl', 'wb')
		pickle.dump(my_tasks, pkl_out)
		pkl_out.close()	
		raise SystemExit

print
print '*' * 15
print "Task List Manager"
print '*' * 15

while True:
	print
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, 's' for a summary, 'n' to add new, 'd' to delete or 'e' to exit\n.:")
	script_response(user_input)

