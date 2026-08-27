"""
Problem: Calculate Monthly Income and Savings

Description:
Write a Python program that asks the user to enter their monthly salary, freelance income, and monthly
expenses. Calculate and display the total monthly income, monthly savings, and savings percentage.

Formulas:
Total Income = Salary + Freelance Income
Monthly Savings = Total Income - Monthly Expenses
Savings Percentage = (Monthly Savings / Total Income) × 100

Expected Interaction:
Enter monthly salary: 50000
Enter monthly freelance income: 10000
Enter monthly expenses: 45000

Total Monthly Income: 60000.00
Monthly Savings: 15000.00
Savings Percentage: 25.00%
"""

monthly_salary = float(input("Enter monthly salary: "))
monthly_freelance_income = float(input("Enter monthly freelance income: "))
monthly_expenses = float(input("Enter monthly expenses: "))

total_monthly_income = monthly_salary + monthly_freelance_income
monthly_savings = total_monthly_income - monthly_expenses
savings_percentage = (monthly_savings / total_monthly_income) * 100

print(f"\nTotal Monthly Income: {total_monthly_income:.2f}")
print(f"Monthly Savings: {monthly_savings:.2f}")
print(f"Savings Percentage: {savings_percentage:.2f}%")