# basic task list script
# currently python 2.7

from datetime import date
import pickle

print
print '*' * 15
print "Task List Manager"
print '*' * 15

#import saved task list from file, create if doesn't exits
pkl_file = open('myfile.pkl', 'rb+')
tasks = pickle.load(pkl_file) 
pkl_file.close()

user_input = ""

def script_response(user_input):
	"""takes in a string used to determine a control flow
		of output responses"""
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks[user_input] = date.today()
		print "\t Task", user_input, "added to task list"
	elif user_input == 'd':
		if tasks:
			sorted = tasks.items()
			sorted.sort()
			for key, value in sorted:
				print "\t", value, key
			user_input = raw_input("\nTask to delete: ")
			if user_input not in tasks:
				print "\t That task does not exist."
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
	print
	print '-' * 15
	print "Instructions:"
	user_input = raw_input("Press 'l' to list tasks, n' to add new, 'd' to delete or 'e' to exit\n.:")
	script_response(user_input)

