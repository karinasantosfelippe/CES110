"""
Author: Karina Felippe
Purpose: Formatting strings.
Similar with Sample Solution? Y
"""

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
sentence = f'{last_name}, {first_name} {last_name}'.title()
print(f'Your name is {sentence}')