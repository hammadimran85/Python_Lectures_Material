import math

while True:
    start = input('Do you want use a Basic Calculator or a Scientific (b/s): ').lower()
    if start == 'b':
        print("Options for Basic Calculator:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
    elif start == 's':
        print("Enter 'sqrt' for square root")
        print("Enter 'exp' for exponentiation")
        print("Enter 'ln' for natural logarithm")
        print("Enter 'log' for base 10 logarithm")
        print("Enter 'sin' for sine")
        print("Enter 'cos' for cosine")
        print("Enter 'tan' for tangent")
        print("Enter 'asin' for arcsine")
        print("Enter 'acos' for arccosine")
        print("Enter 'atan' for arctangent")
        print("Enter 'sinh' for hyperbolic sine")
        print("Enter 'cosh' for hyperbolic cosine")
        print("Enter 'tanh' for hyperbolic tangent")
        print("Enter 'pi' for Pi (π)")
        print("Enter 'e' for Euler's number (e)")
        print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "sqrt":
        num = float(input("Enter a number: "))
        result = math.sqrt(num)
    elif user_input == "exp":
        num = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = math.pow(num, exponent)
    elif user_input == "ln":
        num = float(input("Enter a number: "))
        result = math.log(num)
    elif user_input == "log":
        num = float(input("Enter a number: "))
        result = math.log10(num)
    elif user_input == "sin":
        num = float(input("Enter a number (in radians): "))
        result = math.sin(num)
    elif user_input == "cos":
        num = float(input("Enter a number (in radians): "))
        result = math.cos(num)
    elif user_input == "tan":
        num = float(input("Enter a number (in radians): "))
        result = math.tan(num)
    elif user_input == "asin":
        num = float(input("Enter a number (between -1 and 1): "))
        result = math.asin(num)
    elif user_input == "acos":
        num = float(input("Enter a number (between -1 and 1): "))
        result = math.acos(num)
    elif user_input == "atan":
        num = float(input("Enter a number: "))
        result = math.atan(num)
    elif user_input == "sinh":
        num = float(input("Enter a number: "))
        result = math.sinh(num)
    elif user_input == "cosh":
        num = float(input("Enter a number: "))
        result = math.cosh(num)
    elif user_input == "tanh":
        num = float(input("Enter a number: "))
        result = math.tanh(num)
    elif user_input == "pi":
        result = math.pi
    elif user_input == "e":
        result = math.e
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "add":
            result = num1 + num2
        elif user_input == "subtract":
            result = num1 - num2
        elif user_input == "multiply":
            result = num1 * num2
        elif user_input == "divide":
            result = num1 / num2
        else:
            print("Invalid input")
            continue

    print("Result: " + str(result))
