"""
Problem: Calculate Salary After Deduction

Description:
Write a Python program that asks the user to enter the basic salary and deduction percentage. Calculate
the deduction amount and the net salary after deduction.

Formulas:
Deduction Amount = (Basic Salary × Deduction Percentage) / 100
Net Salary = Basic Salary - Deduction Amount

Expected Interaction:
Enter basic salary: 50000
Enter deduction percentage: 8
Deduction Amount: 4000.00
Net Salary: 46000.00
"""

basic_salary = float(input("Enter basic salary: "))
deduction_percentage = float(input("Enter deduction percentage: "))

deduction_amount = (basic_salary * deduction_percentage) / 100
net_salary = basic_salary - deduction_amount

print(f"Deduction Amount: {deduction_amount:.2f}")
print(f"Net Salary: {net_salary:.2f}")