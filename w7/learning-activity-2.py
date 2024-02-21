"""
Author: Karina Felippe
Purpose: Practice writing basic functions.
"""

'''
## Team Activity week 2

square_area = float(input("Square side: "))
square_area = square_area ** 2
print(f'The area of the square is: {square_area}\n')

rectangle_length = float(input('Rectangle length: '))
rectangle_width = float(input('Rectangle width: '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area}\n')

radius = float(input("Circle radius: "))
cicle_area = 3.14 * (radius ** 2)
print(f'The area of the circle is: {cicle_area}')

# stretch 1
print('Stretch 1:')
import math

radius = float(input("Circle radius: "))
cicle_area = math.pi * (radius ** 2)
print(f'The area of the circle is: {cicle_area}')

# stretch 2
print('Stretch 2:')
print(f"The area is {square_area} cm^2. And the area in meters is: {square_area / 10000} m^2.")
'''


## ACTIVITY

import math

## SQUARE AND RECTANGLE
def compute_area_rectangle(length_param, width_param):
    return length_param * width_param

## CIRCLE
def compute_area_circle(radius_param):
    cicle_area = math.pi * (radius_param ** 2)
    return cicle_area


## USER INTERACTION
user_input = ""

while user_input != "quit":
    user_input = input("What kind of shape you have? (Type 'quit' to end.) ").lower()

    if user_input == "square":
        side_input = float(input("Square side: "))
        square_area = compute_area_rectangle(side_input, side_input)
        print(f'The area of the square is: {square_area}\n')
    elif user_input == "rectangle":
        rectangle_length = float(input('Rectangle length: '))
        rectangle_width = float(input('Rectangle width: '))
        rectangle_area = compute_area_rectangle(rectangle_length, rectangle_width)
        print(f'The area of the rectangle is: {rectangle_area}\n')
    elif user_input == "circle":
        radius = float(input("Circle radius: "))
        cicle_area = compute_area_circle(radius)
        print(f'The area of the circle is: {cicle_area}')
    else:
        print("Invalid input. Please try again.")
