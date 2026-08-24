"""
Problem: Calculate Monthly Expense Percentage

Description:
Write a Python program that asks the user to enter their monthly income, rent, food expense, and transportation 
expense. Calculate and display the total monthly expenses, remaining money, and the percentage of income spent.

Formulas:
Total Expenses = Rent + Food + Transportation
Remaining Money = Income - Total Expenses
Percentage Spent = (Total Expenses / Income) × 100

Expected Interaction:
Enter monthly income: 50000
Enter monthly rent: 15000
Enter monthly food expense: 8000
Enter monthly transportation expense: 4000

Total Monthly Expenses: 27000.00
Remaining Money: 23000.00
Percentage of Income Spent: 54.00%
"""

monthly_income = float(input("Enter monthly income: "))
monthly_rent = float(input("Enter monthly rent: "))
monthly_food_expense = float(input("Enter monthly food expense: "))
monthly_transportation_expense = float(input("Enter monthly transportation expense: "))

total_monthly_expenses = (
    monthly_rent
    + monthly_food_expense
    + monthly_transportation_expense
)

remaining_money = monthly_income - total_monthly_expenses
percentage_spent = (total_monthly_expenses / monthly_income) * 100

print(f"\nTotal Monthly Expenses: {total_monthly_expenses:.2f}")
print(f"Remaining Money: {remaining_money:.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2f}%")