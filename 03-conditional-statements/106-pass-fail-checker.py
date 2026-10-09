"""
Problem: Pass or Fail Checker

Description:
Write a Python program that asks the user to enter an exam mark.
If the mark is greater than or equal to 50, display "Pass".
Otherwise, display nothing.

Condition:
Pass → mark >= 50

Expected Interaction:
Enter a mark: 75

Pass
"""

mark = int(input("Enter a mark: "))

if mark >= 50:
    print("Pass")