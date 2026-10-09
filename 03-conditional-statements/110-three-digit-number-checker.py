"""
Problem: Three-Digit Number Checker

Description:
Write a Python program that asks the user to enter an integer.
Check whether the number is between 100 and 999, inclusive.
If both conditions are satisfied, display "Three-Digit Number".
Otherwise, display nothing.

Condition:
Three-Digit Number → 100 <= number <= 999

Expected Interaction:
Enter a number: 456

Three-Digit Number
"""

number = int(input("Enter a number: "))

if 100 <= number <= 999:
    print("Three-Digit Number")