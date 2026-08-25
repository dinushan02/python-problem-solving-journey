"""
Problem: Calculate Age in Years and Months

Description:
Write a Python program that asks the user to enter their age in months. Calculate and display the age
in complete years and remaining months.

Formulas:
Years = Total Months // 12
Remaining Months = Total Months % 12

Expected Interaction:
Enter age in months: 290
Age: 24 years and 2 months
"""

age_in_months = int(input("Enter age in months: "))

years = age_in_months // 12
remaining_months = age_in_months % 12

print(f"\nAge: {years} years and {remaining_months} months")