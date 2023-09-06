print("*** Enhanced Calculator ***")

calculation_history = []

while True:

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    operation = int(input("What Operation you want to Perform? : "))

    if operation == 5:
        print("Thank you for using the Enhanced Calculator!")
        break

    if 1 <= operation <= 4:
        operator = ""
        if operation == 1:
            result = num1 + num2
            operator = "+"
        elif operation == 2:
            result = num1 - num2
            operator = "-"
        elif operation == 3:
            result = num1 * num2
            operator = "*"
        elif operation == 4:
            if num2 != 0:
                result = num1 / num2
                operator = "/"
            else:
                result = "Division by zero is not allowed."

        print('Answer: {} {} {} = {}'.format(num1, operator, num2, result))
        calculation_history.append('{} {} {} = {}'.format(num1, operator, num2, result))

    else:
        print("Choose between 1 to 5 ...")

    view_history = input("Do you want to view calculation history? (yes/no): ")
    if view_history.lower() == "yes":
        if calculation_history:
            print("Calculation History:")
            for entry in calculation_history:
                print(entry)
        else:
            print("No calculation history yet.")
