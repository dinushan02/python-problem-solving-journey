"""
Problem: Calculate Number of Notes

Description:
Write a Python program that stores an amount of money and calculates how many 
100-unit notes are required to represent that amount.

Assumption:
The amount is perfectly divisible by 100.

Formula:
Number of Notes = Amount // 100

Expected Output:
Number of 100-unit notes: 50
"""

amount = 5000

number_of_notes = amount // 100

print(f"Number of 100-unit notes: {number_of_notes}")