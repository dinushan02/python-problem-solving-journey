"""
Problem: Calculate Daily Average Expense

Description:
Write a Python program that asks the user to enter monthly food, transportation, and entertainment
expenses. Calculate and display the total monthly expenses and average daily expense.

Assumption:
The month has 30 days.

Formulas:
Total Monthly Expenses = Food + Transportation + Entertainment
Average Daily Expense = Total Monthly Expenses / 30

Expected Interaction:
Enter monthly food expense: 9000
Enter monthly transportation expense: 3000
Enter monthly entertainment expense: 3000

Total Monthly Expenses: 15000.00
Average Daily Expense: 500.00
"""

monthly_food_expense = float(input("Enter monthly food expense: "))
monthly_transportation_expense = float(input("Enter monthly transportation expense: "))
monthly_entertainment_expense = float(input("Enter monthly entertainment expense: "))

total_monthly_expenses = (
    monthly_food_expense
    + monthly_transportation_expense
    + monthly_entertainment_expense
)

average_daily_expense = total_monthly_expenses / 30

print(f"\nTotal Monthly Expenses: {total_monthly_expenses:.2f}")
print(f"Average Daily Expense: {average_daily_expense:.2f}")