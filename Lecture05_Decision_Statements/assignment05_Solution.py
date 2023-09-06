print("Welcome to the Text-Based Quiz!")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "choices": ["a) Karachi", "b) Islamabad", "c) Lahore", "d) Kpk"],
        "correct_answer": "b",
        "feedback": "Correct! Islamabad is the capital of Pakistan."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "correct_answer": "b",
        "feedback": "Correct! Mars is known as the Red Planet."
    },
]

score = 0

user_answer = input("Press Enter to start the quiz...")

# Question 1
print(questions[0]["question"])
print(questions[0]['choices'])
answer = input("Your answer: ").lower()
if answer == questions[0]["correct_answer"]:
    print(questions[0]["feedback"])
    score += 1
else:
    print("Incorrect. The correct answer is:", questions[0]["correct_answer"])
user_answer = input("Press Enter to continue...")

# Question 2
print(questions[1]["question"])
print(questions[1]['choices'])
answer = input("Your answer: ").lower()
if answer == questions[1]["correct_answer"]:
    print(questions[1]["feedback"])
    score += 1
else:
    print("Incorrect. The correct answer is:", questions[1]["correct_answer"])
user_answer = input("Press Enter to continue...")


print("\nYou scored", score, "out of", len(questions))
