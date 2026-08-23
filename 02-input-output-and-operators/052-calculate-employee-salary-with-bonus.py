"""
Problem: Calculate Employee Salary with Bonus

Description:
Write a Python program that asks the user to enter the basic salary and bonus percentage. Calculate the
bonus amount and the total salary after adding the bonus.

Formulas:
Bonus Amount = (Basic Salary × Bonus Percentage) / 100
Total Salary = Basic Salary + Bonus Amount

Expected Interaction:
Enter basic salary: 50000
Enter bonus percentage: 10
Bonus Amount: 5000.00
Total Salary: 55000.00
"""

basic_salary = float(input("Enter basic salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))

bonus_amount = (basic_salary * bonus_percentage) / 100
total_salary = basic_salary + bonus_amount

print(f"Bonus Amount: {bonus_amount:.2f}")
print(f"Total Salary: {total_salary:.2f}")