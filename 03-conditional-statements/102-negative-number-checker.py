"""
Problem: Negative Number Checker

Description:
Write a Python program that asks the user to enter a number. Check whether the number is 
less than 0. If it is less than 0, display "Negative Number".

Expected Interaction:
Enter a number: -15

Negative Number
"""

number = float(input("Enter a number: "))

if number < 0:
    
    print("Negative Number")