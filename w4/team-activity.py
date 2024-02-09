'''
Author: Karina Felippe
Purpose: Group practice

# version 1.0
magic_number = input("What is the magic number? ")
guess = input("What is your guess? ")

if guess == magic_number:
    print("You guessed it!")
elif guess < magic_number:
    print("Lower")
else:
    print("Higher")

# version 1.1
magic_number = input("What is the magic number? ")
guess = input("What is your guess? ")

while guess != magic_number:
    if guess > magic_number:
        print("Higher")
    elif guess < magic_number:
        print("Lower")
    guess = input("What is your guess? ")
print("You guessed it!")


# version 2.0

import random

number = random.randint(1, 100)

guess = int(input("What is your guess? "))

while guess != number:
    if guess > number:
        print("Higher")
    elif guess < number:
        print("Lower")
    guess = int(input("What is your guess? "))
print("You guessed it!")


# version 3.1 - stretch challenge 1
import random

number = random.randint(1, 100)

guess = int(input("What is your guess? "))
attempt = 1

while guess != number:
    attempt += 1
    if guess > number:
        print("Higher")
    elif guess < number:
        print("Lower")
    guess = int(input("What is your guess? "))
print("You guessed it!")
print(f"Attempt: {attempt}")

'''


# version 3.2 - stretch challenge 2
import random

print("Guess My Number Game")

answer = 'yes'

while answer == 'yes': 
    number = random.randint(1, 100)

    guess = int(input("What is your guess? "))
    attempt = 1

    while guess != number:
        attempt += 1
        if guess > number:
            print("Higher")
        elif guess < number:
            print("Lower")
        guess = int(input("What is your guess? "))
    
    print(f"\nYou guessed it!\nAttempt: {attempt}\n")

    answer = input("Do you want to play again? ")

print("End game.")