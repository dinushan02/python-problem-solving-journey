"""
Problem: Calculate Commission Amount and Total Earnings

Description:
Write a Python program that asks the user to enter the base salary, sales amount, and commission percentage.
Calculate and display the commission amount and total earnings.

Formulas:
Commission Amount = (Sales Amount × Commission Percentage) / 100
Total Earnings = Base Salary + Commission Amount

Expected Interaction:
Enter base salary: 40000
Enter sales amount: 100000
Enter commission percentage: 5

Commission Amount: 5000.00
Total Earnings: 45000.00
"""

base_salary = float(input("Enter base salary: "))
sales_amount = float(input("Enter sales amount: "))
commission_percentage = float(input("Enter commission percentage: "))

commission_amount = (sales_amount * commission_percentage) / 100
total_earnings = base_salary + commission_amount

print(f"\nCommission Amount: {commission_amount:.2f}")
print(f"Total Earnings: {total_earnings:.2f}")