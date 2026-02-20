def number():
    userInput = int(input("Enter number: "))
    userInput1 = int(input("Enter number: "))
    userInput2 = int(input("Enter number: "))

    largest = max(userInput, userInput1, userInput2)

    print(largest)

number()