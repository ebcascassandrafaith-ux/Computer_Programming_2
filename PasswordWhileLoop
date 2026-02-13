
while True:
    enterPass = input("Enter Password: ").lower()
    letter = False
    number = False

    for char in enterPass:
        if (char.isalpha()):
            letter = True
        elif (char.isdigit()):
            number = True

    if not letter:
        print("Invalid Password, Try Again! Must contain letter")
    elif not number:
        print("Invalid Password, Try Again! Must contain number")
    elif (len(enterPass)) < 8:
        print("Invalid Password, Try Again! Must contain more than 8 characters")
    else: 
        print("Yey! Password Accepted")
        break 