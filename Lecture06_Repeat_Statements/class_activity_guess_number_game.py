print('Welcome to Guess a Number')

min_range = int(input('Enter the first number: '))
max_range = int(input('Enter the second number: '))

import random
correct_answer = random.randint(min_range , max_range)

max_attempts = 5
attempt = 0

while attempt <= max_attempts:
    guess = int(input('Enter a number to guess correct answer between {} and {}: '.format(min_range,max_range)))

    attempt += 1

    if guess > correct_answer:
        print('Your guess is a large number')
    elif guess < correct_answer:
        print('Your guess is a smaller number')
    else:
        print('You guess correctly!')
        print(f'You guess the correct answer in {attempt}')
        break
else:
    print(f'You are out of attempts and correct answer is {correct_answer} ...please try again')
