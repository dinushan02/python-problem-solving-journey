"""
Problem: Greater of Two Numbers

Description:
Write a Python program that asks the user to enter two different
integers. If the first number is greater than the second number,
display "First Number is Greater". Otherwise, display
"Second Number is Greater".

Condition:
First Number is Greater → num1 > num2
Second Number is Greater → num1 < num2

Expected Interaction 1:
Enter the first number: 25
Enter the second number: 10

First Number is Greater

Expected Interaction 2:
Enter the first number: 8
Enter the second number: 17

Second Number is Greater
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("First Number is Greater")
else:
    print("Second Number is Greater")