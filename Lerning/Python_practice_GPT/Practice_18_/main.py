class TaskStack:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def finish_task(self):
        if self.is_empty():
            return None
        return self.tasks.pop()

    def show_tasks(self):
        if self.is_empty():
            return None
        
        for t in range(len(self.tasks)):
            print(self.tasks[t])

    def is_empty(self):
        return len(self.tasks) == 0

def save_tasks(task, filename):
    with open(filename, "w") as f:
        for i in task:
            f.write(f"{i}\n")

filename = r"C:\Users\Chirayu\Documents\GitHub\Lern_python_Me\Lerning\Python_practice_GPT\Practice_18_\task.txt"
tasks = TaskStack()

tasks.add_task("Study Python")
tasks.add_task("Finish homework")
tasks.add_task("Read book")

print("Finished:", tasks.finish_task())

tasks.show_tasks()

save_tasks(tasks.tasks, filename)

