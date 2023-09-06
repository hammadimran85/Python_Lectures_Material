#Assignment02
word = input("Enter a word: ")
print("Word length:", len(word))
print("Contains digits:", any(char.isdigit() for char in word))
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Reverse:", word[::-1])

d = {'r':1}

#Assignment Bonus Task (Compulsory)
is_palindrome = word == word[::-1]
print("Palindrome:", is_palindrome)
char_frequency = {}
for char in word:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
print("Character Frequency:")
for char, freq in char_frequency.items():
        print(f"{char}: {freq}")

# Advance Bonus Task
password = input('Enter a Password: ')
criteria_met = 0

if len(password) >= 8:
    criteria_met += 1

if any(char.isupper() for char in password):
    criteria_met += 1

if any(char.islower() for char in password):
    criteria_met += 1

if any(char.isdigit() for char in password):
    criteria_met += 1

if any(char in '!@#$%^&*' for char in password):
    criteria_met += 1

if "password" not in password.lower():
    criteria_met += 1

if criteria_met >= 4:
        first_three = password[:3]
        last_three = password[-3:]
        new_password = first_three + last_three + str(len(password))
if criteria_met == 4:
    print("Password Strength: Strong")
    print("New password:", new_password)
elif 1 <= criteria_met <= 3:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Weak")
remainder = 2
remainder /= 5
print(remainder)