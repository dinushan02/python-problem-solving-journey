"""
Problem: Calculate Average Monthly Expense

Description:
Write a Python program that asks the user to enter expenses for four weeks. Calculate and display the
total monthly expense and average weekly expense.

Formulas:
Total Monthly Expense = Week 1 + Week 2 + Week 3 + Week 4
Average Weekly Expense = Total Monthly Expense / 4

Expected Interaction:
Enter expense for week 1: 12000
Enter expense for week 2: 15000
Enter expense for week 3: 13000
Enter expense for week 4: 10000

Total Monthly Expense: 50000.00
Average Weekly Expense: 12500.00
"""

week1_expense = float(input("Enter expense for week 1: "))
week2_expense = float(input("Enter expense for week 2: "))
week3_expense = float(input("Enter expense for week 3: "))
week4_expense = float(input("Enter expense for week 4: "))

total_monthly_expense = (
    week1_expense
    + week2_expense
    + week3_expense
    + week4_expense
)

average_weekly_expense = total_monthly_expense / 4

print(f"\nTotal Monthly Expense: {total_monthly_expense:.2f}")
print(f"Average Weekly Expense: {average_weekly_expense:.2f}")