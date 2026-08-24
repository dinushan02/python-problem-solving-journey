"""
Problem: Calculate Remaining Time and Percentage Spent

Description:
Write a Python program that asks the user to enter the total time in minutes and the time already spent.
Calculate and display the remaining time and the percentage of time spent.

Formulas:
Remaining Time = Total Time - Time Spent
Percentage Spent = (Time Spent / Total Time) × 100

Expected Interaction:
Enter total time in minutes: 120
Enter time spent in minutes: 45
Remaining Time: 75.00 minutes
Percentage Spent: 37.50%
"""

total_time_in_minutes = float(input("Enter total time in minutes: "))
time_spent_in_minutes = float(input("Enter time spent in minutes: "))

remaining_time = total_time_in_minutes - time_spent_in_minutes
percentage_spent = (time_spent_in_minutes / total_time_in_minutes) * 100

print(f"Remaining Time: {remaining_time:.2f} minutes")
print(f"Percentage Spent: {percentage_spent:.2f}%")