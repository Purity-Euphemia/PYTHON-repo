print("TO_DO_LIST_MANAGER")
print("LIST OF MENU FUNTIONS")
print("""
MENU 
	1. Add a task.
	2. View tasks.
	3. Mark tasks as complete.
	4. Delete a task.
	5. Exit.
	""")
number = int(input('Enter your choice from 1 to 5 to pick a MENU: '))
match number:
		
		case 1:
			print ('ADD A TASK')
			number1 = input('Enter the task: ')
			cart = ["buy groceries", "finisher work"]
			while(True):
				if number1 == "1":
					print("add a task")
					break
				else:
					print("invalid input")
					break
		case 2:
			print ('VIEW TASKS')
			number2 = input('Enter the task: ')
			cart = ["buy groceries", "finisher work"]
			while(True):
				if number2 == "2":
					print("view tasks")
					break
				else:
					print("invalid input")
					break
		case 3:
			print ('MARK TASK AS COMPLETE')
			number3 = input('Enter the task: ')
			cart = ["buy groceries", "finisher work"]
			while(True):
				if number3 == "3":
					print("mark task as complete")
					break
				else:
					print("invalid input")
					break
		case 4:
			print ('DELETE A TASK')
			number4 = input('Enter the task: ')
			cart = ["buy groceries", "finisher work"]
			while(True):
				if number4 == "4":
					print("delete a task")
					break
				else:
					print("invalid input")
					break
		case 5:
			print ('EXIT')
			number5 = input('Enter the task: ')
			cart = ["buy groceries", "finisher work"]
			while(True):
				if number5 == "5":
					print("exist")
					break
				else:
					print("invalid input")
					break




























