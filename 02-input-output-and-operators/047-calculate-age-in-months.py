"""
Problem: Calculate Age in Months

Description:
Write a Python program that asks the user to enter their age in years and calculates 
their approximate age in months.

Formula:
Age in Months = Age in Years × 12

Expected Interaction:
Enter your age in years: 24
Approximate Age in Months: 288
"""

age_in_years = int(input("Enter your age in years: "))

age_in_months = age_in_years * 12

print(f"Approximate Age in Months: {age_in_months}")