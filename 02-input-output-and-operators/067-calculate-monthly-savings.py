"""
Problem: Calculate Monthly Savings

Description:
Write a Python program that asks the user to enter their monthly income, rent, food expense, transportation expense, 
and other monthly expenses. Calculate and display the total monthly expenses and monthly savings.

Formulas:
Total Expenses = Rent + Food + Transportation + Other Expenses
Monthly Savings = Income - Total Expenses

Expected Interaction:
Enter monthly income: 50000
Enter monthly rent: 15000
Enter monthly food expense: 8000
Enter monthly transportation expense: 4000
Enter other monthly expenses: 3000

Total Monthly Expenses: 30000.00
Monthly Savings: 20000.00
"""

monthly_income = float(input("Enter monthly income: "))
monthly_rent = float(input("Enter monthly rent: "))
monthly_food_expense = float(input("Enter monthly food expense: "))
monthly_transportation_expense = float(input("Enter monthly transportation expense: "))
other_monthly_expenses = float(input("Enter other monthly expenses: "))

total_expenses = (
    monthly_rent
    + monthly_food_expense
    + monthly_transportation_expense
    + other_monthly_expenses
)

monthly_savings = monthly_income - total_expenses

print(f"\nTotal Monthly Expenses: {total_expenses:.2f}")
print(f"Monthly Savings: {monthly_savings:.2f}")