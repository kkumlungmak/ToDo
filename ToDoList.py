def AddTask(ToDo):
    with open("Todo.txt","a") as list:
        list.write(ToDo + "\n")

def ReadList():
    os.system('clear')
    print("My Tasks List:")
    with open("Todo.txt", "r") as task:
        print(task.read())

def Remove(task):
    with open("Todo.txt", "r") as list:
        list = list.read()
        list = list.splitlines()
    open("ToDo.txt","w").close()
    for item in list:
        if item != task:
            AddTask(item)
import os
from datetime import datetime
os.system('clear')

input("Hi There!\n\nPress Enter to Proceed...")
while(1):
    ReadList()
    print("Enter 'a' to add tasks.")
    print("Enter 'e' to remove tasks.")
    print("Enter 'x' to exit program.")
    WantTo = input("What do you want?: ")
    if WantTo == "a":
        while(1):
            ReadList()
            ToDo = input("Enter your Task (enter blank to stop): ")
            if ToDo == " " or ToDo == "":
                break
            AddTask(ToDo)
    elif WantTo == "x" :
        os.system('clear')
        print("Bye!")
        break
    elif WantTo == "e" :
        while(1):
            ReadList()
            task = input("What task do you want to remove? (enter blank to stop)\n>>> ")
            if task == " " or task == "" :
                break
            Remove(task)
