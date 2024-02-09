'''
Author: Karina Santos Felippe
Version: 1.0
'''

'''
Version: 1.0


grade = int(input("What is your grade percentage? (1-100) "))
letter = 'F'

#Determine the letter grade
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

print(f"Your letter grade is: {letter}")

if grade >= 70:
    print("Congratularions! You passed!")
else:
    print("I am sorry, you don't passed. You will get it next time!")
'''


grade = int(input("What is your grade percentage? (1-100) \n"))
letter = 'F'

#Determine the letter grade
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

# Stretch Challenge
sign = ''
if letter != 'F':
    grade_last_digit = grade % 10

    if grade_last_digit >= 7:
        sign = '+'
    elif grade >= 93:
        sign = ''
    elif grade_last_digit < 3:
        sign = '-'

print(f"\nYour letter grade is: {letter}{sign}\n")

if grade >= 70:
    print("Congratularions! You passed!")
else:
    print("I am sorry, you don't passed. You will get it next time!")
    