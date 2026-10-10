"""
Problem: Pass or Fail Checker

Description:
Write a Python program that asks the user to enter an exam mark.
If the mark is greater than or equal to 50, display "Pass".
Otherwise, display "Fail".

Condition:
Pass → mark >= 50
Fail → mark < 50

Expected Interaction 1:
Enter your mark: 75

Pass

Expected Interaction 2:
Enter your mark: 35

Fail
"""

mark = int(input("Enter your mark: "))

if mark >= 50:
    print("Pass")
else:
    print("Fail")