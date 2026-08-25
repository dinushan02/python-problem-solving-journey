"""
Problem: Convert Total Seconds to Minutes and Seconds

Description:
Write a Python program that asks the user to enter a total number of seconds. Calculate and display the
complete minutes and remaining seconds.

Formulas:
Minutes = Total Seconds // 60
Remaining Seconds = Total Seconds % 60

Expected Interaction:
Enter total seconds: 245

Minutes: 4
Remaining Seconds: 5
"""

total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"\nMinutes: {minutes}")
print(f"Remaining Seconds: {remaining_seconds}")