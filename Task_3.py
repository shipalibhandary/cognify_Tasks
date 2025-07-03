class Task:

    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name

    def display(self):
        print(f"Number: {self.task_id} | {self.name}")


tasks = []
taskcounter = 1


def create_task():
    global taskcounter
    yourtask = input("Enter your tasks: ")
    task = Task(taskcounter, yourtask)
    tasks.append(task)
    taskcounter += 1


def display_task():
    if tasks:
        for task in tasks:
            task.display()
            print()
    else:
        print("Your task list is Empty!!!!")


def delete_task():
    id = int(input("\nEnter the Task_id that you want to delete: "))
    for task in tasks:
        if task.task_id == id:
            tasks.remove(task)
        else:
            print("Invalid!!! please check the id again...")





while True:
    print("\n1.create New task\n 2.Display All\n 4.Delete tasks ")
    choice = input("Enter your choice: ")
    if choice == '1':
        create_task()
    elif choice == '2':
        print("\nYour Tasks Are: \n")
        display_task()
    elif choice == '4':
        delete_task()
    else:
        print("Invalid choice!!!....Please try again!!")
