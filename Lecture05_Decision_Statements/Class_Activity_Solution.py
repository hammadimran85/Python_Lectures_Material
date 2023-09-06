marks = int(input('Enter your marks in numbers: '))

if marks >= 90 or marks <= 100:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

if grade == 'A':
    feedback = 'Wxcelient work!'
elif grade == 'B':
    feedback = 'Good Job!'
elif grade == 'C':
    feedback = 'Fair effort!'
elif grade == 'D':
    feedback = 'You are Pass!'
else:
    feedback = 'You are Fail! better luck nexttime!'
print(f'Your grade is {grade}')
print(f'Feedback: {feedback}')

