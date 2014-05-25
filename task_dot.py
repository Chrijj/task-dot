# basic task list script
# currently python 2.7
# 0.1 - formatting and consistency updates
# 0.0 - basic list input

print '*' * 15
print "Task List Manager"
print '*' * 15

tasks = []
user_input = ""

while user_input != 'e':
	print '-' * 15
	user_input = raw_input("Press 'n' to add a new task, 'l' to list tasks or 'e' to exit\n..:")
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks.append(user_input)
		print "Task", user_input, "added to task list\n"
	elif user_input == 'l':
		if len(tasks) == 0:
			print "No Tasks in list"
		else:
			print tasks
	elif user_input == 'e':
		exit
	else:
		print "Invalid input, try again"



