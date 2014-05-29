# basic task list script
# currently python 2.7
# next prioritised changes - adjust style and flow to be object oriented
# 0.5 - added file handling for saving data between sessions
# 0.4 - main control flow moved to a function call, changed ifs to use boolean value of list
# 0.3 - tasks changed from a list to dictionary, task name: todays date
# 0.2 - option to remove tasks
# 0.1 - formatting and consistency updates
# 0.0 - basic list input

from datetime import date
import pickle

print '*' * 15
print "Task List Manager"
print '*' * 15

#import saved task list from file, create if doesn't exits
pkl_file = open('myfile.pkl', 'wb+')
tasks = pickle.load(pkl_file) 
pkl_file.close()
#tasks = {}

user_input = ""

def script_response(user_input):
	"""takes in a string used to determine a control flow
		of output responses"""
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks[user_input] = date.today()
		print "Task", user_input, "added to task list\n"
	elif user_input == 'd':
		if tasks:
			print "Current Tasks:\n",tasks
			user_input = raw_input("Task to delete: ")
			if user_input not in tasks:
				print "That task is not in the list"
			else:
				del tasks[user_input]
				print user_input, "removed from tasks."
		else:
			print "No Tasks in list"
	elif user_input == 'l':
		if tasks:
			print tasks
		else:
			print "No Tasks in list"
	elif user_input == 'e':
		exit
		output = open('myfile.pkl', 'wb')
		pickle.dump(tasks, output)
		output.close()
	else:
		print "Invalid input, try again"

while user_input != 'e':
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, n' to add new, 'd' to delete or 'e' to exit\n.:")
	script_response(user_input)
	


