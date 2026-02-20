def calcu():

 print("Select Operation")
 print("1. Add, 2. Subtract, 3. Multiply, 4. Divide")

 operator = input("Select your operator(1, 2, 3, 4): ")
 firstNum = float(input("Enter number: "))
 secondNum = float(input("Enter number: "))

 if operator == "1":
    addition = firstNum + secondNum
    print(f"The answer is: {addition} ")
 elif operator == "2":
    subtraction = firstNum - secondNum
    print(f"The answer is: {subtraction}")
 elif operator == "3":
    multiplication = firstNum * secondNum
    print(f"The answer is: {multiplication}")
 elif operator == "4":
    division = firstNum / secondNum
    print(f"The answer is: {division}")
 else:
    print("Invalid")

calcu()