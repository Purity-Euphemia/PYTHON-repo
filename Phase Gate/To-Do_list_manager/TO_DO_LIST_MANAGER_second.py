print("TO-DO LIST MANAGER")
print("LIST OF MENU FUNCTIONS")

tasks = [] 
completed = []  

while True:
    print("""
MENUpy
    1. Add a task.
    2. View tasks.
    3. Mark a task as complete.
    4. Delete a task.
    5. Exit.
    """)

    choice = input('Enter your choice (1 to 5): ')

    if choice == "1":
        print("ADD A TASK")
        task = input("Enter the task: ")
        tasks.append(task)
        print(f'Task "{task}" added.\n')

    elif choice == "2":
        print("VIEW TASKS")
        if not tasks:
            print("No tasks found.\n")
        else:
            for count, task in enumerate(tasks):
                status = "✓ Done" if count in completed else "✗ Not done"
                print(f"{count + 1}. {task} [{status}]")
        print()

    elif choice == "3":
        print("MARK TASK AS COMPLETE")
        if not tasks:
            print("No tasks to mark.\n")
        else:
            for count, task in enumerate(tasks):
                print(f"{count + 1}. {task}")
            index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                completed.append(index)
                print(f'Task "{tasks[index]}" marked as complete.\n')
            else:
                print("Invalid task number.\n")

    elif choice == "4":
        print("DELETE A TASK")
        if not tasks:
            print("No tasks to delete.\n")
        else:
            for count, task in enumerate(tasks):
                print(f"{count + 1}. {task}")
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f'Task "{deleted_task}" deleted.\n')
              
                if index in completed:
                    completed.remove(index)
               
                completed = [count-1 if count > index else count for count in completed]
            else:
                print("Invalid task number.\n")

    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.\n")
