"""
Problem: Calculate Employee Overtime Pay

Description:
Write a Python program that asks the user to enter regular hours worked, regular hourly rate, overtime
hours worked, and overtime hourly rate. Calculate and display the regular pay, overtime pay, and total pay.

Formulas:
Regular Pay = Regular Hours × Regular Rate
Overtime Pay = Overtime Hours × Overtime Rate
Total Pay = Regular Pay + Overtime Pay

Expected Interaction:
Enter regular hours worked: 40
Enter regular hourly rate: 500
Enter overtime hours worked: 5
Enter overtime hourly rate: 750

Regular Pay: 20000.00
Overtime Pay: 3750.00
Total Pay: 23750.00
"""

regular_hours_worked = float(input("Enter regular hours worked: "))
regular_hourly_rate = float(input("Enter regular hourly rate: "))
overtime_hours_worked = float(input("Enter overtime hours worked: "))
overtime_hourly_rate = float(input("Enter overtime hourly rate: "))

regular_pay = regular_hours_worked * regular_hourly_rate
overtime_pay = overtime_hours_worked * overtime_hourly_rate

total_pay = regular_pay + overtime_pay

print(f"\nRegular Pay: {regular_pay:.2f}")
print(f"Overtime Pay: {overtime_pay:.2f}")
print(f"Total Pay: {total_pay:.2f}")