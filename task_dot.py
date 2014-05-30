# basic task list script
# currently python 2.7
# next prioritised changes - adjust style and flow to be object oriented, improve readme and move revision history to there
# 0.6 - adjusted printing of tasks to loop through all entries, indented machine responses to improve readability, fixed bug to correctly save pickled data to file
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
		print "\t Task", user_input, "added to task list\n"
	elif user_input == 'd':
		if tasks:
			print "\t Current Tasks:\n",tasks
			user_input = raw_input("Task to delete: ")
			if user_input not in tasks:
				print "\t That task is does not exist."
			else:
				del tasks[user_input]
				print "\t", user_input, "removed from tasks."
		else:
			print "\t No Tasks in list"
	elif user_input == 'l':
		if tasks:
			sorted = tasks.items()
			sorted.sort()
			for key, value in sorted:
				print "\t", value, key
		else:
			print "\t No Tasks in list"
	elif user_input == 'e':
		output = open('myfile.pkl', 'wb')
		pickle.dump(tasks, output)
		output.close()
		exit
	else:
		print "\t Invalid input, try again"

while user_input != 'e':
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, n' to add new, 'd' to delete or 'e' to exit\n.:")
	script_response(user_input)

