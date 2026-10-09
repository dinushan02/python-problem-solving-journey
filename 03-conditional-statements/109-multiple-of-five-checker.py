"""
Problem: Multiple of Five Checker

Description:
Write a Python program that asks the user to enter an integer.
Check whether the number is divisible by 5 without a remainder.
If it is divisible by 5, display "Multiple of Five".
Otherwise, display nothing.

Condition:
Multiple of Five → number % 5 == 0

Expected Interaction:
Enter a number: 25

Multiple of Five
"""

number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Multiple of Five")