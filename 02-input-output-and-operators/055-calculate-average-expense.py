"""
Problem: Calculate Average Expense

Description:
Write a Python program that asks the user to enter three different expenses. Calculate and 
display the average expense.

Formula:
Average Expense = (Expense 1 + Expense 2 + Expense 3) / 3

Expected Interaction:
Enter first expense: 1500
Enter second expense: 2500
Enter third expense: 1000
Average Expense: 1666.67
"""

first_expense = float(input("Enter first expense: "))
second_expense = float(input("Enter second expense: "))
third_expense = float(input("Enter third expense: "))

average_expenses = (first_expense + second_expense + third_expense) / 3

print(f"Average Expense: {average_expenses:.2f}")