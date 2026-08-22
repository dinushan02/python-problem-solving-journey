"""
Problem: Calculate Total Minutes

Description:
Write a Python program that stores the number of days, hours, and minutes 
in separate variables. Convert the entire duration into total minutes.

Formula:
Total Minutes = (Days × 1440) + (Hours × 60) + Minutes

Assumptions:
1 day = 1440 minutes
1 hour = 60 minutes

Expected Output:
Total Minutes: 3210
"""

days = 2
hours = 5
minutes = 30

total_minutes = (days * 1440) + (hours * 60) + minutes

print(f"Total Minutes: {total_minutes}")