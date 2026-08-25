"""
Problem: Convert Total Days to Weeks and Days

Description:
Write a Python program that asks the user to enter a total number of days. Calculate and display the
complete weeks and remaining days.

Formulas:
Weeks = Total Days // 7
Remaining Days = Total Days % 7

Expected Interaction:
Enter total days: 45

Weeks: 6
Remaining Days: 3
"""

total_days = int(input("Enter total days: "))

weeks = total_days // 7
remaining_days = total_days % 7

print(f"\nWeeks: {weeks}")
print(f"Remaining Days: {remaining_days}")