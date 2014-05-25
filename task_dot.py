# basic task list script
# currently python 2.7
# version 0.0

print '*' * 15
print "Task List Manager"
print '*' * 15

tasks = []
user_input = ""

while user_input != 'e':
	print '-' * 15
	user_input = raw_input("\n Press 'n' to add a new task, 'l' to list tasks or 'e' to exit")
	if user_input == 'n':
		user_input = raw_input("Enter the task: ")
		tasks.append(user_input)
	elif user_input == 'l':
		if len(tasks) == 0:
			print "No Tasks in list"
		else:
			print tasks
	else:
		print "Invalid input, try again"

exit


