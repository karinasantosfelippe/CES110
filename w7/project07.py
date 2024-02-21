"""
Author: Karina Santos Felippe

Exceeding requirements: Using range function to iterate and increment the for loop by 5. Preventing user to input something diferent than F/C.
"""

def calculate_windchill(T, V):
    return 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + (0.4275 * T * (V ** 0.16))

def convert_to_fahrenheit(temperature):
    return (temperature * (9 / 5)) + 32

input_temperature = float(input("What is the temperature? "))
input_scale = ""
temperature = 0

while True:
    input_scale = input("Fahrenheit or Celsius (F/C)? ").upper()

    if input_scale == "C":
        temperature = convert_to_fahrenheit(input_temperature)
        break
    elif input_scale == "F":
        temperature = input_temperature
        break
    else:
        print("Invalid input. Please try again.")

for wind_speed in range(5, 61, 5):
    windchill = calculate_windchill(temperature, wind_speed)
    print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")