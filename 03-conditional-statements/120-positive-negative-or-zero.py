"""
Problem: Positive, Negative, or Zero

Description:
Write a Python program that asks the user to enter an integer.
If the number is greater than 0, display "Positive Number".
If the number is less than 0, display "Negative Number".
Otherwise, display "Zero".

Conditions:
Positive Number → num1 > 0
Negative Number → num1 < 0
Zero → Otherwise

Expected Interaction 1:
Enter a number: 15

Positive Number

Expected Interaction 2:
Enter a number: -8

Negative Number

Expected Interaction 3:
Enter a number: 0

Zero
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")