"""
Author: Karina Felippe
Purpose: Practicing while loops


"""

'''
number = 0

# Keep looping as long as the number is less than 10
while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")

# Start with the number 1
number = 1

# Keep looping as long as the number is less than or equal to 5
while number <= 5:
    # Display the number
    print(f"The number is: {number}")

    # Update the number to be one more than it was
    number = number + 1 

print("Finished with the loop")


# BAD EXAMPLE: This code does not define a value for the number before it is used
# In the following example, the program will cause an error because it tries to check of number is less than 10, but the variable does not exist yet.

while number < 10: # ERROR, number is not defined yet
    number = int(input("What is the number? "))

print("Finished with the loop")    


# GOOD EXAMPLE: This code correctly sets the variable to a value before it is used
#The following example corrects the mistake by declaring the variable and setting it equal to a value prior to the loop.

number = 0

while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")


# BAD EXAMPLE: This code sets the variable to a number that prevents the code from ever entering the loop.

number = 25 # ERROR: This number is greater than 10, so the loop will not run

while number < 10: # This body of this loop will NEVER run
    number = int(input("What is the number? "))

print("Finished with the loop")


# OK EXAMPLE: This code sets the variable to a number that allows the loop to run. But it is not great, because it sets it to a non-standard value of 6.

number = 6 # This number is less than 10, so the loop will run, but it is not standard

while number < 10: # This body of this loop will run just fine
    number = int(input("What is the number? "))

print("Finished with the loop")    



# GOOD EXAMPLE: This code sets the variable to a number that allows the loop to run. It uses a standard initialization value of 0.

number = 0 # This number is less than 10, and is a standard value

while number < 10: # This body of this loop will run just fine
    number = int(input("What is the number? "))

print("Finished with the loop")    


##### Activities:

### 1. Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))
    
print(f"The number is: {number}")

'''


### Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

response = ''

while response != 'yes':
    response = input("May I have a piece of candy? ")

print("Thank you.")