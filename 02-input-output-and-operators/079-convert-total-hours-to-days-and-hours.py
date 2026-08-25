"""
Problem: Convert Total Hours to Days and Hours

Description:
Write a Python program that asks the user to enter a total number of hours. Calculate and display the
complete days and remaining hours.

Formulas:
Days = Total Hours // 24
Remaining Hours = Total Hours % 24

Expected Interaction:
Enter total hours: 53

Days: 2
Remaining Hours: 5
"""

total_hours = int(input("Enter total hours: "))

days = total_hours // 24
remaining_hours = total_hours % 24

print(f"\nDays: {days}")
print(f"Remaining Hours: {remaining_hours}")