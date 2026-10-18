"""
Problem: Number Range Checker

Description:
Write a Python program that asks the user to enter an integer.
If the number is between 1 and 100, inclusive, display
"Number is Within Range". Otherwise, display
"Number is Outside Range".

Condition:
Within Range → 1 <= num <= 100
Outside Range → Otherwise

Expected Interaction 1:
Enter a number: 75

Number is Within Range

Expected Interaction 2:
Enter a number: 150

Number is Outside Range
"""

num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("Number is Within Range")
else:
    print("Number is Outside Range")