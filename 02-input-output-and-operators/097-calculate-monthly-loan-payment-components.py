"""
Problem: Calculate Loan Repayment with Simple Interest

Description:
Write a Python program that asks the user to enter the loan amount, annual interest rate, and loan period
in years. Calculate and display the simple interest, total repayment, and average yearly repayment.

Formulas:
Simple Interest = (Loan Amount × Annual Interest Rate × Loan Period) / 100
Total Repayment = Loan Amount + Simple Interest
Average Yearly Repayment = Total Repayment / Loan Period

Expected Interaction:
Enter loan amount: 100000
Enter annual interest rate: 8.8
Enter loan period in years: 5.5

Simple Interest: 48400.00
Total Repayment: 148400.00
Average Yearly Repayment: 26981.82
"""

loan_amount = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
loan_period_years = float(input("Enter loan period in years: "))

simple_interest = (loan_amount * annual_interest_rate * loan_period_years) / 100
total_repayment = loan_amount + simple_interest
average_yearly_repayment = total_repayment / loan_period_years

print(f"\nSimple Interest: {simple_interest:.2f}")
print(f"Total Repayment: {total_repayment:.2f}")
print(f"Average Yearly Repayment: {average_yearly_repayment:.2f}")