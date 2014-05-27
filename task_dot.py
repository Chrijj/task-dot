# basic task list script
# currently python 2.7
# 0.3 - changed to make tasks a dictionary with the key being the task name and the value being the date
# 0.2 - option to remove tasks
# 0.1 - formatting and consistency updates
# 0.0 - basic list input

from datetime import date

print '*' * 15
print "Task List Manager"
print '*' * 15

tasks = {}
user_input = ""

while user_input != 'e':
	print '-' * 15
	user_input = raw_input("Press 'n' to add a new task, 'd' to delete a task, 'l' to list tasks or 'e' to exit\n..:")
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks[user_input] = date.today()
		print "Task", user_input, "added to task list\n"
	elif user_input == 'd':
		if len(tasks) == 0:
			print "No Tasks in list"
		else:
			print "Current Tasks:\n",tasks
			user_input = raw_input("Task to delete: ")
			if user_input not in tasks:
				print "That task is not in the list"
			else:
				del tasks[user_input]
				print user_input, "removed from tasks."
	elif user_input == 'l':
		if len(tasks) == 0:
			print "No Tasks in list"
		else:
			print tasks
	elif user_input == 'e':
		exit
	else:
		print "Invalid input, try again"



