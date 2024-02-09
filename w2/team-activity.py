"""
Author: Karina Felippe

Add                         |   +    |
Subtract                    |   -    |
Multiply                    |   *    |
Divide                      |   /    |
Divide and drop remainder   |   //   |
Exponent                    |   **   |
Remainder or Modulus        |   %    |
"""

#green

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