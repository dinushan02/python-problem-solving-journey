"""
Problem: Calculate Total Seconds

Description:
Write a Python program that stores the number of hours, minutes, and seconds 
in separate variables. Convert the entire duration into total seconds.

Formula:
Total Seconds = (Hours × 3600) + (Minutes × 60) + Seconds

Expected Output:
Total Seconds: 9015
"""

hours = 2
minutes = 30
seconds = 15

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print(f"Total Seconds: {total_seconds}")