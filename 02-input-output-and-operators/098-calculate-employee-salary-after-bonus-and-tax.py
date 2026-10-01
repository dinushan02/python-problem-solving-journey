"""
Problem: Calculate Employee Salary After Bonus and Tax

Description:
Write a Python program that asks the user to enter the basic salary, bonus percentage, and tax percentage.
Calculate and display the bonus amount, salary after bonus, tax amount, and final salary after tax.

Formulas:
Bonus Amount = (Basic Salary × Bonus Percentage) / 100
Salary After Bonus = Basic Salary + Bonus Amount
Tax Amount = (Salary After Bonus × Tax Percentage) / 100
Final Salary = Salary After Bonus - Tax Amount

Expected Interaction:
Enter basic salary: 50000
Enter bonus percentage: 10
Enter tax percentage: 8

Bonus Amount: 5000.00
Salary After Bonus: 55000.00
Tax Amount: 4400.00
Final Salary: 50600.00
"""

basic_salary = float(input("Enter basic salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))
tax_percentage = float(input("Enter tax percentage: "))

bonus_amount = (basic_salary * bonus_percentage) / 100
salary_after_bonus = basic_salary + bonus_amount
tax_amount = (salary_after_bonus * tax_percentage) / 100
final_salary_after_tax = salary_after_bonus - tax_amount

print(f"\nBonus Amount: {bonus_amount:.2f}")
print(f"Salary After Bonus: {salary_after_bonus:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Salary: {final_salary_after_tax:.2f}")