"""
Problem: Voting Eligibility Checker

Description:
Write a Python program that asks the user to enter their age.
If the age is greater than or equal to 18, display
"Eligible to Vote". Otherwise, display "Not Eligible to Vote".

Conditions:
Eligible to Vote → age >= 18
Not Eligible to Vote → age < 18

Expected Interaction 1:
Enter your age: 21

Eligible to Vote

Expected Interaction 2:
Enter your age: 16

Not Eligible to Vote
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")