"""
Problem: Smaller of Two Numbers

Description:
Write a Python program that asks the user to enter two different
integers. If the first number is smaller than the second number,
display "First Number is Smaller". Otherwise, display
"Second Number is Smaller".

Condition:
First Number is Smaller → num1 < num2
Second Number is Smaller → num1 > num2

Expected Interaction 1:
Enter the first number: 8
Enter the second number: 17

First Number is Smaller

Expected Interaction 2:
Enter the first number: 25
Enter the second number: 10

Second Number is Smaller
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    print("First Number is Smaller")
else:
    print("Second Number is Smaller")