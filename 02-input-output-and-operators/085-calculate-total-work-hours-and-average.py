"""
Problem: Calculate Total Work Hours and Average

Description:
Write a Python program that asks the user to enter the number of hours worked on five different days.
Calculate and display the total work hours and average work hours per day.

Formulas:
Total Work Hours = Day 1 + Day 2 + Day 3 + Day 4 + Day 5
Average Work Hours = Total Work Hours / 5

Expected Interaction:
Enter hours worked on day 1: 8
Enter hours worked on day 2: 7.5
Enter hours worked on day 3: 9
Enter hours worked on day 4: 8.5
Enter hours worked on day 5: 7

Total Work Hours: 40.00
Average Work Hours Per Day: 8.00
"""

hours_worked_day1 = float(input("Enter hours worked on day 1: "))
hours_worked_day2 = float(input("Enter hours worked on day 2: "))
hours_worked_day3 = float(input("Enter hours worked on day 3: "))
hours_worked_day4 = float(input("Enter hours worked on day 4: "))
hours_worked_day5 = float(input("Enter hours worked on day 5: "))

total_worked_hours = (
    hours_worked_day1
    + hours_worked_day2
    + hours_worked_day3
    + hours_worked_day4
    + hours_worked_day5
)

average_work_hours_per_day = total_worked_hours / 5

print(f"\nTotal Work Hours: {total_worked_hours:.2f}")
print(f"Average Work Hours Per Day: {average_work_hours_per_day:.2f}")