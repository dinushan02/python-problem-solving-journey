"""
Problem: Convert Seconds to Minutes and Seconds

Description:
Write a Python program that stores a total number of seconds and converts it 
into complete minutes and remaining seconds.

The program should use:
- Integer division (//) to calculate complete minutes.
- Modulus (%) to calculate remaining seconds.

Expected Output:
Minutes: 2
Remaining Seconds: 5
"""

total_seconds = 125

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"Minutes: {minutes}")
print(f"Remaining Seconds: {remaining_seconds}")