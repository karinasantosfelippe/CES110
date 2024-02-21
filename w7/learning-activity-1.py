"""
Author: Karina Felippe
Purpose: Practice writing basic functions.
"""

'''
# First define the function
def print_message():
    print("Hello CSE 110 World!")

# Call the function now
print_message()

# Call it again here
print_message()



def print_double(value):
    double_value = value * 2
    print(double_value)

print_double(12) # outputs 24
print_double(3) # outputs 6
print_double(42) # outputs 84



def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4)


# Variable Scope:

## !! BAD EXAMPLE !!
def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4)

# ERROR: This does not work, because the variable "double_value" is only alive during
# the body of the function. Down here, we have chosen to give the return value the name "new_number"
print(double_value) # BAD CODE

## GOOD EXAMPLE
def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = "Message 1"
print_message(the_message)

# but it also works to use a different variable...
user_message = "Message 2"
print_message(user_message)
'''


## ACTIVITY

def display_regular(the_message):
    print(the_message)

def display_uppercase(the_message):
    print(str(the_message).upper())

def display_lowercase(the_message):
    print(str(the_message).lower())

user_message = input("What is your message? ")
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)