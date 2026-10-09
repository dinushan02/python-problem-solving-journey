"""
Problem: Odd Number Checker

Description:
Write a Python program that asks the user to enter an integer.
Check whether the number is odd. If the remainder after
dividing the number by 2 is not 0, display "Odd Number".

Formula:
Odd Number → number % 2 != 0

Expected Interaction:
Enter a number: 15

Odd Number
"""

number = int(input("Enter a number: "))

if number % 2 != 0:
    print("Odd Number")