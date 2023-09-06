total = 0
for i in range(1,10,4):
    # total += i
    print(i)

list = [5,4,3,2,1]

for i in list:
    print("*" * i)

while True:
    age = input("Enter your age: ")
    if age.isdigit() and 0 < int(age) <= 120:
        break
    else:
        print("Invalid input. Please enter a valid age.")
print(f"Your age is {age}.")


while True:
    print('This is endless loop')

import time
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
print("Boom!")
