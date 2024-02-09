"""
Author: Karina Felippe
Purpose: Numeric Variables

Operators:
Add                         |   +    |
Subtract                    |   -    |
Multiply                    |   *    |
Divide                      |   /    |
Divide and drop remainder   |   //   |
Exponent                    |   **   |
 (To the power of)
Remainder or Modulus        |   %    |
 (Get the remainder that 
 would result from dividing
 the first number by the
 second one.)
"""

'''
number = 7
print(f"The number is {number}.")

color = 'blue'
animal = 'horse'

# You can add, or concatenate, two strings together with +:
print(color + animal)
# This displays: bluehorse

# You can add many strings together, whether the strings are variables or directly in
# the quotation marks:
print(color + ' ' + animal + '!')
# This displays: blue horse!

# You can also save the result into a new string variable:
combined_words = color + ' ' + animal + '!'
print(combined_words)

boys_count = 10
girls_count = 12

# Add two numbers together using the + operator:
print(boys_count + girls_count)
# This displays: 22

# You can save the result in a new variable to use later:
total_count = boys_count + girls_count
print(total_count)

apple_count = 5

# Error on this line... You can't add strings and integers together!
print("You have " + apple_count + " apples") # ERROR!

# This creates a new integer variable with the value of 10
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 50
width_num = 10

# If you add the numbers together, you would get the result you expect:
print(length_num + width_num) # This displays: 60

# You can convert the values to the strings "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)

# The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_string + width_string) # This displays: 5010

quantity_from_user = input("How many items do you have? ")

# The variable quantity_from_user is a string.
# To convert it to an integer you use the int(...) notation:
quantity_number = int(quantity_from_user)

# Because the quantity_number variable is an integer you can do math with it:
double_number = quantity_number * 2

# If you want to use these values in strings, you CANNOT just add them, you first
# have to convert them to a string:

# WRONG:
print("Twice as many is: " + double_number)

# Right:
double_string = str(double_number)
print("Twice as many is: " + double_string)

# You can also do this in one step:
# Right:
print("Twice as many is " + str(double_number))

# Using two lines:
people_string = input("\nHow many people are in the room? ")
people_number = int(people_string)
print(people_number)

# Using one line:
people_number = int(input("How many people are in the room? "))
print(people_number)

# The same works for floating point numbers:
length_number = float(input("What is the length? "))
print(f"Length is {length_number:.2f} with 2 decimal point.\n")

'''


'''
For this assignment, you will practice several different examples, but they should all be part of the same program.

Write a program that does the following:
1. Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
2. Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
3. Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

Here is an example of the tasks when run:

#
How old are you? 25
On your next birthday, you will be 26

How many egg cartons do you have? 3
You have 36 eggs

How many cookies do you have? 18
How many people are there? 8
Each person may have 2.25 cookies
#

Verify that your program works correctly by following each step in this testing procedure:

1. Run through the entire program using the inputs shown in the example above. Make sure your output matches the output shown above.
2. For the first question, regarding ages, try entering the ages 18 and 59 (one at a time), and ensure that the program correctly outputs the numbers 19 and 60 for the next birthdays.
3. For the second question, regarding eggs, try entering a 5 and 0 (one at a time), and ensure that the program outputs 60 and 0 eggs.
4. For the third question, regarding cookies, trying entering two more sets of values (one at a time) and make sure the division works correctly. Try one set of values that results in an even number (no decimal part) and one that results in a decimal and make sure they both work correctly.
5. Double check that the output matches the example output exactly, including:
    - The numeric values should appear in the middle of the other words, not on a separate line.
    - The number of spaces before and after the numbers should match the example output.
    - There should be a blank line before each section.

'''

age_number = int(input("\nHow old are you? "))
print(f"On your next birthday, you will be { age_number + 1 }.")

egg_number = int(input("\nHow many egg cartons do you have? "))
print(f"You have { egg_number * 12 } eggs.")

cookies_number = int(input("\nHow many cookies do you have? "))
people_number = int(input("How many people are there? "))
print(f"Each person may have { (cookies_number / people_number) } cookies.\n")