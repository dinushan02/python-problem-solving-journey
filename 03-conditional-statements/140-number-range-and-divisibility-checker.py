"""
Problem: Number Range and Divisibility Checker

Description:
Check whether an integer is between 1 and 100
(inclusive) and divisible by 5.

Conditions:
- The number must be between 1 and 100.
- The number must be divisible by 5.
- If both conditions are satisfied, display "Valid Number".
- Otherwise, display "Invalid Number".

Expected Interaction:

Enter a number: 25
Valid Number

Enter a number: 105
Invalid Number

Enter a number: 24
Invalid Number
"""

num = int(input("Enter a number: "))

if 1 <= num <= 100 and num % 5 == 0:
    print("Valid Number")
else:
    print("Invalid Number")