"""
Problem: Calculate Remaining Amount

Description:
Write a Python program that stores an amount of money and determines the remaining amount 
after dividing it into 100-unit notes.

The program should use the modulus operator (%) to calculate the remainder.

Expected Output:
Remaining Amount: 75
"""

amount = 5275

remaining_amount = amount % 100

print(f"Remaining Amount: {remaining_amount}")