"""
Problem: Multiple Condition Number Checker

Description:
Check whether an integer is divisible by both 2 and 7.

Conditions:
- If the number is divisible by both 2 and 7,
  display "Divisible by Both 2 and 7".
- Otherwise, display "Not Divisible by Both 2 and 7".

Expected Interaction:

Enter a number: 28
Divisible by Both 2 and 7

Enter a number: 15
Not Divisible by Both 2 and 7
"""

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 7 == 0:
    print("Divisible by Both 2 and 7")
else:
    print("Not Divisible by Both 2 and 7")