"""
Problem: Voting Eligibility Checker

Description:
Write a Python program that asks the user to enter their age.
If the age is greater than or equal to 18, display
"Eligible to Vote". Otherwise, display nothing.

Condition:
Voting Eligibility → age >= 18

Expected Interaction:
Enter your age: 21

Eligible to Vote
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")