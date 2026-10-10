"""
Problem: Even or Odd Number Checker

Description:
Write a Python program that asks the user to enter an integer.
If the number is divisible by 2 without a remainder, display
"Even Number". Otherwise, display "Odd Number".

Conditions:
Even Number → number % 2 == 0
Odd Number → number % 2 != 0

Expected Interaction 1:
Enter a number: 24

Even Number

Expected Interaction 2:
Enter a number: 15

Odd Number
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")