"""
Problem: Password Strength Category Checker

Description:
Categorize a password based on its length.

Conditions:
- Length less than 6: Weak Password.
- Length from 6 to 9: Medium Password.
- Length greater than or equal to 10: Strong Password.

Expected Interaction:

Enter your password: abc
Weak Password

Enter your password: python123
Medium Password

Enter your password: python12345
Strong Password
"""

password = input("Enter your password: ")

password_length = len(password)

if password_length < 6:
    print("Weak Password")
elif 6 <= password_length < 10:
    print("Medium Password")
else:
    print("Strong Password")