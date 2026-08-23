"""
Problem: Calculate Difference of Two Numbers

Description:
Write a Python program that asks the user to enter two numbers, calculates the difference between 
the first number and the second number, and displays the result.

Formula:
Difference = First Number - Second Number

Expected Interaction:
Enter first number: 50
Enter second number: 18
Difference: 32
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

difference = num1 - num2

print(f"Difference: {difference}")