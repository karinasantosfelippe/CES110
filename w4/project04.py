'''
Author: Karina Santos Felippe
Purpose: Word Puzzle Project

Exceeding Requirements: the system will random select a word from a list of words.
'''
import random
words = ["faith", "baptism", "family", "exaltation", "liahona"]
secret_word = random.choice(words)

print("Welcome to the Word Guessing Game!\n")

# Loop to generate the initial hint
hint = ""
for letter in secret_word:
    hint += "_ "
print(f"Your hint is: {hint}")

user_guess = input("\nWhat is your guess? ")
guess_count = 1
# If the guess is correct, we don't need to iterate anything
while user_guess != secret_word:
    # initialize the hint
    hint = ""
    # prevent use to digit capitalized letter
    user_guess = user_guess.lower()
    # prevent user to write words that are greater than the hint
    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        # iterate the letters in user guess to create the hint
        for i in range(len(user_guess)):
            # rule 1: check if the letter is present in the secret word at that exact spot (uppercase).
            if user_guess[i] == secret_word[i]:
                hint += user_guess[i].capitalize()
            # If the letter is not at that exact spot, than:
            ## rule 2: check if the letter is present in the secret word, but in a different spot (lowercase).
            elif secret_word.find(user_guess[i]) != -1:
                hint += user_guess[i]
            ## rule 3: the letter is not present at all in the secret word (underscore _).
            else:
                hint += "_"
            # Add a space for hint visualization be better
            hint += " "
        # print the hint to the user
        print(f"Your hint is: {hint}")
    user_guess = input("\nWhat is your guess? ")
    guess_count += 1

print("\nCongratulations! You guessed it!")
print(f"It took you {guess_count} guesses.\n")