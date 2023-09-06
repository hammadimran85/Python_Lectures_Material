print("*** Basic Calculator ***")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = int(input("What Operation you want to Perform? : "))

if operation == 1:
    result = num1 + num2
    print('Answer : {}'.format(int(result)))
elif operation == 2:
    result = num1 - num2
    print('Answer : {}'.format(int(result)))
elif operation == 3:
    result = num1 * num2
    # print('Answer : {}'.format(int(result)))
    print((f'Answer : {int(result)}'))
elif operation == 4:
    if num2 != 0:
        result = num1 / num2
        print('Answer : {}'.format(result))
    else:
        result = "Division by zero is not allowed."
else:
    print("Choose Between 1 to 4 ...")
