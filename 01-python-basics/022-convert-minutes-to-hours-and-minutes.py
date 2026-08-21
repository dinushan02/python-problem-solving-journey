"""
Problem: Convert Minutes to Hours and Minutes

Description:
Write a Python program that stores a total number of minutes and 
converts it into hours and remaining minutes.

The program should use:
- Integer division (//) to calculate complete hours.
- Modulus (%) to calculate remaining minutes.

Expected Output:
Hours: 2
Remaining Minutes: 15
"""

total_minutes = 135

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"Hours: {hours}")
print(f"Remaining Minutes: {remaining_minutes}")