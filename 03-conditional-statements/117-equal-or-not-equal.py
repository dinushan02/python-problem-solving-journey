"""
Problem: Equal or Not Equal

Description:
Write a Python program that asks the user to enter two integers.
If both numbers are equal, display "Numbers are Equal".
Otherwise, display "Numbers are Not Equal".

Conditions:
Equal → num1 == num2
Not Equal → num1 != num2

Expected Interaction 1:
Enter the first number: 10
Enter the second number: 10

Numbers are Equal

Expected Interaction 2:
Enter the first number: 10
Enter the second number: 20

Numbers are Not Equal
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("Numbers are Equal")
else:
    print("Numbers are Not Equal")