"""
Problem: Largest of Three Numbers

Description:
Write a Python program that asks the user to enter three
different integers. Determine which number is the largest.
Display the corresponding message.

Conditions:
First Number is Largest → num1 > num2 and num1 > num3
Second Number is Largest → num2 > num1 and num2 > num3
Third Number is Largest → Otherwise

Expected Interaction:
Enter the first number: 10
Enter the second number: 25
Enter the third number: 15

Second Number is Largest
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("First Number is Largest")
elif num2 > num1 and num2 > num3:
    print("Second Number is Largest")
else:
    print("Third Number is Largest")