"""
Author: Karina Felippe
Purpose: Practicing with list indexes.

"""

'''

the_list = [12.24, 18.50, 4.99, 21.75]

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

print(f"First: {first}, Second: {second}")

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

print(user_choice)



books = []

books.append("1 Nephi")
books.append("2 Nephi")
books.append("Jacob")
books.append("Enos")

print(f"The number of books is: {len(books)}")
for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen.

books.pop(1) # Removes the item at index 3

for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}")

books.pop() # Removes the last item

for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}")

'''

## ACTIVITY
### Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."
### Then complete the following:
### 1. Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.
### 2. Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk
### 3. Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.


shopping_list = []
item = None
print("Please enter the items of the shopping list (type: quit to finish):")

while True:
    item = input("Item: ").lower()
    if item != "quit":
        shopping_list.append(item.capitalize())
        continue
    break

if len(shopping_list) > 0:
    print("\nThe shopping list is: ")
    for item in shopping_list:
        print(item)

    print("\nThe shopping list with indexes is:")
    for i in range(len(shopping_list)):
        print(f"{i}. {shopping_list[i]}")

    print()
    # asking for the index to change 
    index = int(input("\nWhich item would you like to change? "))
    # preventing errors
    while index >= len(shopping_list):
        print("You cannot write a item that do not exist on the list. Please, try again.")
        index =  int(input("\nWhich item would you like to change? "))

    item = input("What is the new item? ").capitalize()
    # changing the item
    shopping_list[index] = item

    print("\nThe shopping list with indexes is:")
    for i in range(len(shopping_list)):
        print(f"{i}. {shopping_list[i]}")
else:
    print("You don`t have any items in your list.")