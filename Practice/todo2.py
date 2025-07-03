class TodoTask:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        if type (task) != str:
            raise ValueError("Inavalid task")
        self.tasks.append([[],task.lower()])


    def view_tasks(self):
        for task in self.tasks:
            print(f"{task[0]} {task[1]}")



t1 = TodoTask()
t1.add_task("going clubbing.....")
