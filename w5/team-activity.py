"""
Author: Karina Santos Felippe
Activity:
    Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
    Once you have a list, have your program do the following:
        1. Compute the sum, or total, of the numbers in the list.
        2. Compute the average of the numbers in the list.
        3. Find the maximum, or largest, number in the list.
"""
from statistics import mean
numbers = []

print("Enter a list of numbers, type 0 when finished.")
user_input = int(input("Enter number: "))
while user_input != 0:
    numbers.append(user_input)
    user_input = int(input("Enter number: "))

if len(numbers) != 0:
    sum_number = sum(numbers)
    print(f"The sum is: {sum_number}")

    average_number = mean(numbers)
    print(f"The average is: {average_number}")

    largest_number = max(numbers)
    print(f"The largest number is: {largest_number}")

    ## Stretch challenge 1
    if largest_number > 0:
        smallest_positive_number = largest_number
        for item in numbers:
            if item >= 0 and item < smallest_positive_number:
                smallest_positive_number = item
        print(f"The smallest positive number is: {smallest_positive_number}")

    ## Stretch challenge 2
    print("\nThe sorted list is:")
    numbers.sort()
    for item in numbers:
        print(item)