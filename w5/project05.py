"""
Author: Karina Santos Felippe
Exceeding requirements: I added a function to print a list with the pattern "{index} - {item}", or the pattern "{index}. {item} - ${price} - quantity: {}" if there is a secondary list. Also, I am preventing user to input a invalid action number, and making actions with empty lists.
In adiction, I am added the quantity of items to add, and the total contabilize the quantity.

Disclaimer: I would used the function sum() to print the total, but I did as the instructions for this assignments.
"""

print("\nWelcome to the Shopping Cart Program!")

menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
shopping_cart = []
prices = []
quantity = []

# function to print the index + item in any list, or index + item + append
def printing_list(sentence, the_list, secondary_list):
    print(sentence)
    for i in range(len(the_list)):
        if secondary_list:
            print(f"{i+1}. {the_list[i]} - ${prices[i]:.2f} - quantity: {quantity[i]}")
            continue
        print(f"{i+1}. {the_list[i]}")

user_choice = '0'
while user_choice != '5':
    printing_list("\nPlease select one of the following:", menu, False)
    user_choice = input("Please enter an action: ")
    # OPTION 1. ADD
    if user_choice == '1':
        new_item = input("What ITEM would you like to add? ").capitalize()
        if new_item not in shopping_cart:
            item_price = float(input(f"What is the PRICE of {new_item}? "))
            item_quantity = int(input(f"What is the QUANTITY of the {new_item} that you want to add? "))
            if item_quantity < 1:
                print("Invalid number. Please try again.")
                continue
            shopping_cart.append(new_item)
            prices.append(item_price)
            quantity.append(item_quantity)
        else:
            for i in range(len(shopping_cart)):
                if shopping_cart[i] == new_item:
                    item_quantity = int(input(f"What is the QUANTITY of the {new_item} that you want to add? "))
                    if item_quantity < 1:
                        print("Invalid number. Please try again.")
                        break
                    quantity[i] += item_quantity
                    break
        print(f"'{new_item}' has been added to the cart.")
    # OPTION 2. VIEW
    elif user_choice == '2':
        if len(shopping_cart) < 1:
            print("You don`t have items in your list yet. If you want to view the shopping cart, you need to select the action to add items at first.")
            continue
        printing_list("The contents of the shopping cart are:", shopping_cart, True)
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
        quantity.pop(item_number)
        print("Item removed.")
    # OPTION 4. TOTAL
    elif user_choice == '4':
        total = 0
        for i in range(len(prices)):
            total += (prices[i] * quantity[i])
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    # OPTION 5. QUIT
    elif user_choice == '5':
        break
    # PREVENT INVALID ANSWER
    else:
        print("Please enter a valid answer!")

print("Thank you. Goodbye.")