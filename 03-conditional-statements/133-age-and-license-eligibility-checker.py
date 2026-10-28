"""
Problem: Age and License Eligibility Checker

Description:
Write a Python program that asks the user to enter their age
and whether they have a driving license. If the age is 18 or
above and the user has a driving license, display
"Eligible to Drive". Otherwise, display "Not Eligible to Drive".

Condition:
age >= 18 and driving_license == "yes"

Expected Interaction 1:
Enter your age: 25
Do you have a driving license: yes

Eligible to Drive

Expected Interaction 2:
Enter your age: 16
Do you have a driving license: yes

Not Eligible to Drive
"""

age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license: ").lower()

if age >= 18 and driving_license == "yes":
    print("Eligible to Drive")
else:
    print("Not Eligible to Drive")