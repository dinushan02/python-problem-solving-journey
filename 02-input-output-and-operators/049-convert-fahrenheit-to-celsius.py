"""
Problem: Convert Fahrenheit to Celsius

Description:
Write a Python program that asks the user to enter a temperature in Fahrenheit, converts it to Celsius,
and displays the result.

Formula:
Celsius = (Fahrenheit - 32) × 5 / 9

Expected Interaction:
Enter temperature in Fahrenheit: 98.6
Celsius: 37.00°C
"""

temperature_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (temperature_in_fahrenheit - 32) * 5 / 9

print(f"Celsius: {celsius:.2f}°C")