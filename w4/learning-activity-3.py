"""
Author: Karina Felippe
Purpose: Practicing for loops


"""

'''

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter) # outputs a 'g' on the screen

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

word = "book"
number_of_letters = len(word) # Notice this can now work for any string

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
print("This is line one.", end=" ")
print("This is line two.")

# version 1
word = "commitment"

for letter in word:
    if(letter == 'm'):
        print(letter.capitalize())
    else:
        print(letter)

# version 2
word = "commitment"
favorite = input("What is your favorite letter? ")

for letter in word:
    if(letter == favorite):
        print(letter.capitalize())
    else:
        print(letter)

'''
        

# version 3
word = "commitment"
favorite = input("What is your favorite letter? ")

for letter in word:
    if(letter == favorite):
        print("_", end="")
    else:
        print(letter, end="")
