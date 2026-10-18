"""
Problem: Smallest of Three Numbers

Description:
Write a Python program that asks the user to enter three
different integers. Determine which number is the smallest.
Display the corresponding message.

Conditions:
First Number is Smallest → num1 < num2 and num1 < num3
Second Number is Smallest → num2 < num1 and num2 < num3
Third Number is Smallest → Otherwise

Expected Interaction:
Enter the first number: 10
Enter the second number: 25
Enter the third number: 5

Third Number is Smallest
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
    print("First Number is Smallest")
elif num2 < num1 and num2 < num3:
    print("Second Number is Smallest")
else:
    print("Third Number is Smallest")