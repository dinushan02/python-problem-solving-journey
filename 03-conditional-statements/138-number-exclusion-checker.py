"""
Problem: Number Exclusion Checker

Description:
Check whether an integer is not divisible by 2.
Display whether the number is odd or even.

Conditions:
- If the number is not divisible by 2, display "Odd Number".
- Otherwise, display "Even Number".

Expected Interaction:

Enter a number: 15
Odd Number

Enter a number: 24
Even Number
"""

num = int(input("Enter a number: "))

if not num % 2 == 0:
    print("Odd Number")
else:
    print("Even Number")