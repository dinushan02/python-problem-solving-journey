"""
Problem: Username and Password Validator

Description:
Write a Python program that asks the user to enter a username
and password. Accept the login only if the username is "admin"
or "user", and the password is "python123". Otherwise, display
"Invalid Credentials".

Conditions:
Valid Username → username == "admin" or username == "user"
Valid Login → Valid Username and password == "python123"

Expected Interaction 1:
Enter username: admin
Enter password: python123

Login Successful

Expected Interaction 2:
Enter username: guest
Enter password: python123

Invalid Credentials
"""

username = input("Enter username: ").lower()
password = input("Enter password: ")

if (username == "admin" or username == "user") and password == "python123":
    print("\nLogin Successful")
else:
    print("Invalid Credentials")