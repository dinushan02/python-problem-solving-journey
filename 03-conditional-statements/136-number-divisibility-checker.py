"""
Problem: Number Divisibility Checker

Description:
Write a Python program that asks the user to enter an integer.
Check whether the number is divisible by both 3 and 5.
If both conditions are satisfied, display
"Divisible by Both 3 and 5". Otherwise, display
"Not Divisible by Both 3 and 5".

Condition:
num % 3 == 0 and num % 5 == 0

Expected Interaction 1:
Enter a number: 15

Divisible by Both 3 and 5

Expected Interaction 2:
Enter a number: 9

Not Divisible by Both 3 and 5
"""

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by Both 3 and 5")
else:
    print("Not Divisible by Both 3 and 5")