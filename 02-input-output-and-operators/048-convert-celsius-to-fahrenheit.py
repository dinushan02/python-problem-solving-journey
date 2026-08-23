"""
Problem: Convert Celsius to Fahrenheit

Description:
Write a Python program that asks the user to enter a temperature in Celsius, converts it to Fahrenheit,
and displays the result.

Formula:
Fahrenheit = (Celsius × 9 / 5) + 32

Expected Interaction:
Enter temperature in Celsius: 25
Fahrenheit: 77.00°F
"""

temperature_in_celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (temperature_in_celsius * 9 / 5) + 32

print(f"Fahrenheit: {fahrenheit:.2f}°F")