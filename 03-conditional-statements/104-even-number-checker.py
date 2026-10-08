"""
Problem: Even Number Checker

Description:
Write a Python program that asks the user to enter an integer. Check whether the number is even. 
If the number is divisible by 2 with no remainder, display "Even Number".

Formula:
Even Number → number % 2 == 0

Expected Interaction:
Enter a number: 24

Even Number
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")