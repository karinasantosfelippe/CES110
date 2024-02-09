"""
Author: Karina Felippe
Purpose: Practicing if statements
"""

'''

x = float(input('x = '))
y = float(input('y = '))
print()

if x > 5 and y > 10:
    print('x > 5 and y > 10')
    # This happens if both conditions are true
else:
    print('FALSE')

if x > 5 or y > 10:
    print('x > 5 or y > 10')
    # This happens if either one of the conditions (or both!) are true
else:
    print('FALSE')

if (x > 5 or x < -5) and y > 10:
    print('(x > 5 or x < -5) and y > 10')
    #In this case, x can either be greater than 5 or less than negative 5, and y must always be greater than 10
else:
    print('FALSE')

if x > 5 or x < -5 and y > 10:
    print('x > 5 or x < -5 and y > 10')
    # Without parentheses, the x < -5 and y > 10 conditions go together and both must be
    # true, unless x > 5, in which case the whole statement is true
else:
    print('FALSE')

is_hot = False

# You can check the value of the variable directly
if is_hot:
    print("It's hot")

# It works, but is redundant (and therefore bad practice) to check if it is True:
if is_hot == True:
    print("It's hot")
    
# Using the "not" keyword
if not is_hot:
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")
    
'''

print("Please, enter a rating from 1-10 on the following questions: \n")
loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

can_loan = False

if loan_size >= 5 :
    if credit_history >= 7 and income >=7:
        can_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
else:
    if credit_history >= 4:
        if income >= 7 or down_payment >= 7:
            can_loan = True
        elif income >= 4 and down_payment >= 4:
            can_loan = True

if can_loan:
    print("\nDecision: yes")
else:
    print("\nDecision: no")