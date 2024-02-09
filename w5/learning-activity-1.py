"""
Author: Karina Felippe
Purpose: Practicing lists

"""

'''
books = []

books.append("1 Nephi")
books.append("2 Nephi")
books.append("Jacob")
books.append("Enos")

print("Your books are:")

for book in books:
    print(book)

receipts = [12.24, 18.50, 4.99, 21.75]

running_total = 0

for receipt in receipts:
    running_total += receipt

# Display the total
print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48

'''

## ACTIVITY:
### Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".
### Hint 1: You should keep asking for friends, as long as the name is not "end". (Does this sound like a loop you know?)
### Hint 2: Be careful not to add "end" to the list of names when it is typed. You can check if the name is or is not something before you add it to the list.

friends = []

while True:
    user_input = input("Type the name of a friend: ").lower()
    if user_input != "end":
        friends.append(user_input.capitalize())
        continue
    break

print("\nYour friends are:")
for name in friends:
    print(name)