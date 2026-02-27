lista = []

while True:
    print("Student Management System")
    print("Main Menu")
    print("A. Show users")
    print("B. Add users")
    print("C. Update user")
    print("D. Delete User")
    print("E. Quit")
    choice = input("Enter letter: ")

    if choice == "A":
        print(lista)

    elif choice == "B":
        add = input("Who do you want to add: ")
        lista.append(add)
        print(lista)

    elif choice == "C":
        update = input("Enter the user you want to update: ")
        if update in lista:
            index = lista.index(update)
            newValue = input("Enter new value: ")
            lista[index] = newValue
        else:
            print("Item not found")

    elif choice == "D":
        deleteSure = input("Enter to delete item: ")
        lista.remove(deleteSure)

    elif choice == "E":
        print("End program. Thank you!")
        exit(0)
    else:
        print("Invalid input")
        


