try:
    with open("messag.txt", "x") as file:
        content = file.read
        print("File Succesfully created")
except FileExistsError:
    print("File Exist Already")

    def sendMessage():
        print("===Messages===")
        with open("messag.txt", "a") as file:
            usermes = input("Enter message: ")
            file.write(usermes)

    def viewMessage():
         print("---=Messages=---")
         file = open("messag.txt", "r")
         print(file.read()+ "\n")
         file.close()

while True:
            print("Main Menu:")
            print("A. Send a message")
            print("B. View all messages")
            print("C. Exit the program")
            choice = input("Enter choice: ").upper()

            if choice == "A":
                 sendMessage()
            elif choice == "B":
                 viewMessage()
            elif choice == "C":
                 break
            else:
                 print("Invalid choice. Try again")
                 continue
                 




