"""
Problem: Calculate Number of Weeks and Days

Description:
Write a Python program that stores a total number of days and converts it 
into complete weeks and remaining days.

Assumption:
1 week = 7 days

The program should use:
- Integer division (//) to calculate complete weeks.
- Modulus (%) to calculate remaining days.

Expected Output:
Weeks: 6
Remaining Days: 3
"""

total_days = 45

weeks = total_days // 7
remaining_days = total_days % 7

print(f"Weeks: {weeks}")
print(f"Remaining Days: {remaining_days}")