while True:
    enterPass = input("Enter Password: ").lower()
    letter = False
    number = False
    variable = any(char.isalpha() for char in enterPass)
    variable1 = any(char.isdigit() for char in enterPass)
    variable2 = len(enterPass) >= 8


    if not variable:
        print("Password must contain a character")
    elif not variable1:
        print("Password must contain numbers")
    elif not variable2:
        print("Characters must be more than 8 characters")
    else:
        print("Yey, Password accepted!")
        break