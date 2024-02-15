"""
Author: Karina Felippe
Purpose: Data in Files

"""

'''
## Finding the Max or Min

numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # This number is larger than the largest we had seen so far

        # So it is now the largest we've seen
        largest_so_far = number

# Now, after the loop we can display it:
print(f"The largest is: {largest_so_far}")


shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

print("version 1")
max_price = -1

for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")

print("version 2")

max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")

'''


## ACTIVITY

people = [
    "Stephanie 3",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = int(people[0].split()[1])
print(youngest_age)

# This will keep track of the person with the youngest age
youngest_name = ""

# Go through each person in the list
for person_line in people:

    parts = person_line.split() # by default this will split on the space

    # Set variables for the two different parts
    name = parts[0]
    age = int(parts[1])

    # Check to see if this current person is younger than the youngest
    # that we have seen so far
    if age <= youngest_age:
        # This person is the new "youngest"

        # Save their age as the new youngest
        youngest_age = age

        # Save their name as the youngest name
        youngest_name = name

# Outside of the loop, so we are all done now
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")