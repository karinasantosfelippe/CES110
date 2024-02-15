"""
Author: Karina Felippe
Purpose: Working with Files

Hint from instructor:
    As shown in the videos, a file can be opened in Python with the following syntax:
        open(filename)

    It's important to close the file after you are finished. A best practice in Python is to use the with syntax so that it will automatically close the file for you when your program leaves that block of code:
        with open(filename) as file_variable:
            # Code to do something with the file goes here

    If the file you were reading from was called colors.txt and you wanted it to be saved into a variable color_file, you would use the following:
        with open("colors.txt") as color_file:
            # Code to do something with the color file goes here
"""

'''

## Reading data from files

with open("colors.txt") as color_file:
    
    for line in color_file:
        # Code to do something with each line goes here


## Splitting a string into pieces

sentence = "I will go and do"

words = sentence.split(" ")
# The variable "words" is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)

'''


## ACTIVITY

with open("sources/books.txt") as book_file:
    for line in book_file:
        book = line.strip()
        print(book)