"""
Problem: Temperature Warning Checker

Description:
Write a Python program that asks the user to enter the
temperature in Celsius. If the temperature is below 0,
display "Freezing Temperature". Otherwise, display nothing.

Condition:
Freezing Temperature → temperature < 0

Expected Interaction:
Enter temperature in Celsius: -5
Freezing Temperature
"""

temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing Temperature")