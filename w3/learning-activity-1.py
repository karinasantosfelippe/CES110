"""
Author: Karina Felippe
Purpose: Practicing if statements

Operators:
Equal to                   |   ==   |
Not equal to               |   !=   |
Greater than               |   >    |
Greater or equal than      |   >=   |
Minor than                 |   <    |
Minor or equal than        |   <=   |
And                        |   and  |
Or                         |   or   |

"""

'''
temperature = float(input("What is the temperature outside? "))
scale = input("Is that Celsius or Fahrenheit (C or F)? ")
if scale.lower() == "f":
    # Convert to Celsius
    temperature = (temperature - 32) * 5/9
if temperature < 0:
    print("It might be snowing outside!")
elif temperature < 23:
    print("It is pleasant outside")
else:
    print("It is getting hot outside")

color = input("What is your favorite color? ")

# This if statement will only match "blue" not "Blue" or "BLUE"
if color == "blue":
    print("I like blue too.")

# This if statement will match the word blue, regardless of the capitalization
if color.lower() == "blue":
    print("I like blue too.")


'''
    
# Comparing Numbers
first_number = int(input("\nWhat is the first number? "))
second_number = int(input("What is the second number? "))

if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")


# Comparing Strings
animal = input("\nWhat is your favorite animal? ")

if animal.lower() == 'horse':
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
