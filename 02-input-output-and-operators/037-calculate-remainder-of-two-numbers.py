"""
Problem: Calculate Remainder of Two Numbers

Description:
Write a Python program that asks the user to enter two numbers, calculates the remainder when the 
first number is divided by the second number, and displays the result.

Expected Interaction:
Enter first number: 17
Enter second number: 5
Remainder: 2
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

remainder = num1 % num2

print(f"Remainder: {remainder}")