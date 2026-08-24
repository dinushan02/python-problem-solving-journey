"""
Problem: Calculate Total Expense

Description:
Write a Python program that asks the user to enter three different expenses. Calculate and 
display the total expense.

Expected Interaction:
Enter first expense: 1500
Enter second expense: 2500
Enter third expense: 1000
Total Expense: 5000.00
"""

first_expense = float(input("Enter first expense: "))
second_expense = float(input("Enter second expense: "))
third_expense = float(input("Enter third expense: "))

total_expenses = first_expense + second_expense + third_expense

print(f"Total Expense: {total_expenses:.2f}")