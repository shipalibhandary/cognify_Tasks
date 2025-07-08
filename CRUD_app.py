import os

class Task:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Id:{self.id} Name: {self.name}")

    def line_by_line(self):
        return f"{self.id},{self.name}\n"

    @staticmethod
    def read_line(line):
        parts = line.strip().split(",")
        if len(parts) ==2:
            id, name=parts
            return Task(int(id), name)
        else:
            print("skipping invalid line",line.strip())
            return None


task_file = "mytasks.txt"
if not os.path.exists(task_file):
    with open(task_file, "w")as f:
        pass

tasks = []

def load():
    with open(task_file, "r")as file:
        for line in file:
            task = Task.read_line(line)
            if task:
                tasks.append(task)

def create_tasks():
    taskid = tasks[-1].id + 1 if tasks else 1
    name = input("Enter task name: ")
    task = Task(taskid, name)
    tasks.append(task)
    save_tasks()
    print("Task Added sucessfully!!!!")

def update_task():
    display_tasks()
    taskid = int(input("Enter the ID of the task to Update: "))
    for task in tasks:
        if task.id == taskid:
            task.name = input("Enter new task Name: ")
            save_tasks()
            print("Task Updated succesfully!!!!")
            return
        else:
            print("Task Not Found!!!!")

def delete_task():
    display_tasks()
    id = int(input("Enter the Id of the task to delete"))
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            print("Task Deleted succesfully!!!!")
            return
    else:
        print("Task UNot Found!!!!")



def display_tasks():
    if tasks:
        for task in tasks:
            task.display()
    else:
        print("No tasks available!!!!")

def save_tasks():
    with open(task_file, "w")as file:
        for task in tasks:
            file.write(task.line_by_line())


load()
while True:
    print("\n.****WELCOME****")
    print("1.Add Task")
    print("2.View Task")
    print("3.update Task")
    print("4.Delete tasks")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        create_tasks()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Existing and saving Tasks...")
        exit(0)
