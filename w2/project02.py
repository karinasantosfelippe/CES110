'''
Author: Karina Santos Felippe
Version: 2.0

Final requirements.
Exceeding requiremtns: the program ask the number of drinks, if the number is higher then zero the program will ask the price of the drink and calculate the drink's subtotal in addition with meal's subtotal.
'''

price_child_meal = float(input("What is the price of a child's meal? $ "))
price_adult_meal = float(input("What is the price of a adult's meal? $ "))
number_children = int(input("What is the number of children? "))
number_adults = int(input("What is the number of adults? "))

number_drink = int(input("\nWhat is the number of drinks? "))
drink_subtotal = number_drink
if number_drink>0:
    drink_price = float(input("What is the price of a drink? $ "))
    drink_subtotal = number_drink * drink_price

subtotal = (price_child_meal * number_children) + (price_adult_meal * number_adults) + drink_subtotal

print(f"\nSubtotal: ${subtotal:.2f}.\n")

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: ${total:.2f}\n")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")