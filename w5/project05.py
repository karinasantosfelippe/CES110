"""
Author: Karina Santos Felippe
Exceeding requirements: I added a function to print a list with the pattern "{index} - {item}", or the pattern "{index}. {item} - ${secondary_item}" if there is a secondary list. Also, I am preventing user to input a invalid action number, and making actions with empty lists.

Disclaimer: I would used the function sum() to print the total, but I did as the instructions for this assignments.
"""

print("\nWelcome to the Shopping Cart Program!")

menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
shopping_cart = []
prices = []

# function to print the index + item in any list, or index + item + append
def printing_list(sentence, the_list, secondary_list):
    print(sentence)
    for i in range(len(the_list)):
        if secondary_list != None:
            print(f"{i+1}. {the_list[i]} - ${secondary_list[i]:.2f}")
            continue
        print(f"{i+1}. {the_list[i]}")

user_choice = '0'
while user_choice != '5':
    printing_list("\nPlease select one of the following:", menu, None)
    user_choice = input("Please enter an action: ")
    # OPTION 1. ADD
    if user_choice == '1':
        new_item = input("What item would you like to add? ").capitalize()
        price = float(input(f"What is the price of {new_item}? "))
        shopping_cart.append(new_item)
        prices.append(price)
        print(f"'{new_item}' has been added to the cart.")
    # OPTION 2. VIEW
    elif user_choice == '2':
        if len(shopping_cart) < 1:
            print("You don`t have items in your list yet. If you want to view the shopping cart, you need to select the action to add items at first.")
            continue
        printing_list("The contents of the shopping cart are:", shopping_cart, prices)
    # OPTION 3. REMOVE
    elif user_choice == '3':
        if len(shopping_cart) < 1:
            print("You don't have items to remove.")
            continue
        item_number = int(input("Which item would you like to remove? ")) - 1
        if item_number >= len(shopping_cart) or item_number < 0:
            print("Please provide a valid item number to remove.")
            continue
        shopping_cart.pop(item_number)
        prices.pop(item_number)
        print("Item removed.")
    # OPTION 4. TOTAL
    elif user_choice == '4':
        total = 0
        for item in prices:
            total += item
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    # OPTION 5. QUIT
    elif user_choice == '5':
        break
    else:
        print("Please enter a valid answer!")

print("Thank you. Goodbye.")