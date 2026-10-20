"""
Problem: Employee Bonus Calculator

Description:
Write a Python program that asks the user to enter their
annual salary. Determine the bonus percentage based on the
salary, calculate the bonus amount, and display the total
salary including the bonus.

Bonus Rules:
Below 30000       → 5%
Below 60000    → 10%
60000 or above    → 15%

Formulas:
Bonus Amount = (Annual Salary * Bonus Percentage) / 100
Total Salary = Annual Salary + Bonus Amount

Expected Interaction:
Enter annual salary: 40000

Annual Salary: 40000.00
Bonus Percentage: 10%
Bonus Amount: 4000.00
Total Salary: 44000.00
"""

annual_salary = float(input("Enter annual salary: "))

if annual_salary < 30000:
    bonus_percentage = 5
elif annual_salary < 60000:
    bonus_percentage = 10
else:
    bonus_percentage = 15

bonus_amount = (annual_salary * bonus_percentage) / 100
total_salary = annual_salary + bonus_amount

print(f"\nAnnual Salary: {annual_salary:.2f}")
print(f"Bonus Percentage: {bonus_percentage}%")
print(f"Bonus Amount: {bonus_amount:.2f}")
print(f"Total Salary: {total_salary:.2f}")