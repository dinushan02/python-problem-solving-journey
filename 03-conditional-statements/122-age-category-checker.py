"""
Problem: Age Category Checker

Description:
Write a Python program that asks the user to enter their age.
If the age is less than 13, display "Child".
If the age is between 13 and 19, inclusive, display "Teenager".
Otherwise, display "Adult".

Conditions:
Child → age < 13
Teenager → 13 <= age <= 19
Adult → Otherwise

Expected Interaction 1:
Enter your age: 10

Child

Expected Interaction 2:
Enter your age: 16

Teenager

Expected Interaction 3:
Enter your age: 25

Adult
"""

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")