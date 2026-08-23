"""
Problem: Calculate Average of Three User Input Numbers

Description:
Write a Python program that asks the user to enter three numbers, calculates their average, 
and displays the result.

Formula:
Average = (Number 1 + Number 2 + Number 3) / 3

Expected Interaction:
Enter first number: 80
Enter second number: 75
Enter third number: 85
Average: 80.00
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print(f"Average: {average:.2f}")