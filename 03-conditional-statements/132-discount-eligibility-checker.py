"""
Problem: Discount Eligibility Checker

Description:
Write a Python program that asks the user to enter their
membership type. If the membership is "gold" or "platinum",
display "Eligible for Special Discount". Otherwise, display
"Not Eligible for Special Discount".

Condition:
membership_type == "gold" or membership_type == "platinum"

Expected Interaction 1:
Enter membership type: gold

Eligible for Special Discount

Expected Interaction 2:
Enter membership type: silver

Not Eligible for Special Discount
"""

membership_type = input("Enter membership type: ").lower()

if membership_type == "gold" or membership_type == "platinum":
    print("Eligible for Special Discount")
else:
    print("Not Eligible for Special Discount")