"""
Problem: Positive or Negative Number

Description:
Write a Python program that asks the user to enter an integer.
If the number is greater than or equal to 0, display
"Non-Negative Number". Otherwise, display "Negative Number".

Conditions:
Non-Negative Number → number >= 0
Negative Number → number < 0

Expected Interaction 1:
Enter a number: 12

Non-Negative Number

Expected Interaction 2:
Enter a number: -8

Negative Number
"""

number = int(input("Enter a number: "))

if number >= 0:
    print("Non-Negative Number")
else:
    print("Negative Number")