import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)


list1 = load_tasks()
def addTask():
    for i in range(0,taskNum):
        val=input("ENTER THE TASKNAME:")
        list1.append(val)

def viewtask():
    for i in list1:
        print(i)
    if len(list1)==0:
        print("No tasks available to view.")

def deleteTask():
    if len(list1) == 0:
        print("No tasks available to delete.")
    else:
        taskToDelete = input("Enter the task you want to delete:")
        list1.remove(taskToDelete)
            
while True:

    print("Welcome to the Task Manager")


    print("1 = You can add tasks.")
    print("2=you can view tasks.")
    print("3=you can delete tasks.")
    print("4=Exit")
    choices= int(input("Enter your choice:"))


    if choices==1:
        taskNum = int(input("How many tasks do you want to add?"))
        addTask()
    elif choices==2:
        viewtask()
    elif choices==3:
        deleteTask()
    else:
        print("Exiting the Task Manager. Goodbye!")
        break




    save_tasks(list1)

print(list1)