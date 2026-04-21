try:
    with open("todolist.txt", "x") as file:
        print("File created succesfully")
except FileExistsError:
    print("This file already exist")
except FileNotFoundError:
    print("File not found")
except:
    print("An error occured")

def addTask():
    with open("todolist.txt", "a") as file:
        task = input("Add task: ")
        file.write(task + "\n")
        print(f"Task {task} added succesfully")

def viewTask():
    with open("todolist.txt", "r") as file:
        print("\n--=To do list=--")
        content = file.read()
        print(content)

while True:
    print("\n--==To do List==--")
    print("Main Menu")
    print("A. Add Tasks")
    print("B. View Task (read)")
    print("C. Exit")
    choice = input("Enter choice: ").upper()

    if choice == "A":
        addTask()
    elif choice == "B":
        viewTask()
    elif choice == "C":
        break
    else:
        print("Invalid input. try again!")
        continue