"""
Problem: Login Credentials Checker

Description:
Write a Python program that asks the user to enter a username
and password. If the username is "admin" and the password is
"python123", display "Login Successful". Otherwise, display
"Invalid Credentials".

Condition:
username == "admin" and password == "python123"

Expected Interaction 1:
Enter username: admin
Enter password: python123

Login Successful

Expected Interaction 2:
Enter username: admin
Enter password: wrongpass

Invalid Credentials
"""

username = input("Enter username: ").lower()
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")