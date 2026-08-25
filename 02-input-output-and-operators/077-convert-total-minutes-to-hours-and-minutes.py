"""
Problem: Convert Total Minutes to Hours and Minutes

Description:
Write a Python program that asks the user to enter a total number of minutes. Calculate and display the
complete hours and remaining minutes.

Formulas:
Hours = Total Minutes // 60
Remaining Minutes = Total Minutes % 60

Expected Interaction:
Enter total minutes: 185

Hours: 3
Remaining Minutes: 5
"""

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"\nHours: {hours}")
print(f"Remaining Minutes: {remaining_minutes}")