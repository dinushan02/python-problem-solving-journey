"""
Problem: Calculate Employee Total Earnings

Description:
Write a Python program that asks the user to enter the basic salary, bonus percentage, overtime pay, and
deduction percentage. Calculate and display the bonus amount, salary after bonus, deduction amount, and final salary.

Formulas:
Bonus Amount = (Basic Salary × Bonus Percentage) / 100
Salary After Bonus = Basic Salary + Bonus Amount
Deduction Amount = (Salary After Bonus × Deduction Percentage) / 100
Final Salary = Salary After Bonus - Deduction Amount + Overtime Pay

Expected Interaction:
Enter basic salary: 50000
Enter bonus percentage: 10
Enter overtime pay: 5000
Enter deduction percentage: 8

Bonus Amount: 5000.00
Salary After Bonus: 55000.00
Deduction Amount: 4400.00
Final Salary: 55600.00
"""

basic_salary = float(input("Enter basic salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))
overtime_pay = float(input("Enter overtime pay: "))
deduction_percentage = float(input("Enter deduction percentage: "))

bonus_amount = (basic_salary * bonus_percentage) / 100
salary_after_bonus = basic_salary + bonus_amount
deduction_amount = (salary_after_bonus * deduction_percentage) / 100
final_salary = salary_after_bonus - deduction_amount + overtime_pay

print(f"\nBonus Amount: {bonus_amount:.2f}")
print(f"Salary After Bonus: {salary_after_bonus:.2f}")
print(f"Deduction Amount: {deduction_amount:.2f}")
print(f"Final Salary: {final_salary:.2f}")