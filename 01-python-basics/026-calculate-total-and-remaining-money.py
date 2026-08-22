"""
Problem: Calculate Total and Remaining Money

Description:
Write a Python program that stores a person's total amount of money and calculates 
the number of 100-unit notes and the remaining money.

The program should use:
- Integer division (//) to calculate the number of notes.
- Modulus (%) to calculate the remaining money.

Expected Output:
Number of 100-unit notes: 52
Remaining Money: 75
"""

amount = 5275

number_of_notes = amount // 100
remaining_money = amount % 100

print(f"Number of 100-unit notes: {number_of_notes}")
print(f"Remaining Money: {remaining_money}")