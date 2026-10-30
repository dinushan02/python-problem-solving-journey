"""
Problem: Divisibility by 3 or 5

Description:
Write a Python program that asks the user to enter an integer.
Check whether the number is divisible by 3 or 5.
If at least one condition is satisfied, display
"Divisible by 3 or 5". Otherwise, display
"Not Divisible by 3 or 5".

Condition:
num % 3 == 0 or num % 5 == 0

Expected Interaction 1:
Enter a number: 9

Divisible by 3 or 5

Expected Interaction 2:
Enter a number: 7

Not Divisible by 3 or 5
"""

num = int(input("Enter a number: "))

if num % 3 == 0 or num % 5 == 0:
    print("Divisible by 3 or 5")
else:
    print("Not Divisible by 3 or 5")