"""
Problem: Bank Loan Eligibility Checker

Description:
Determine whether a customer qualifies for a bank loan
based on age, monthly salary, and credit score.

Conditions:
- Age must be greater than or equal to 21.
- Monthly salary must be greater than or equal to 50000.
- Customer must have a good credit score.
- All three conditions must be satisfied.

Expected Interaction:

Enter your age: 30
Enter monthly salary: 75000
Do you have a good credit score: yes
Loan Approved

Enter your age: 25
Enter monthly salary: 40000
Do you have a good credit score: yes
Loan Rejected
"""

age = int(input("Enter your age: "))
monthly_salary = float(input("Enter monthly salary: "))
good_credit_score = input("Do you have a good credit score: ").lower()

if age >= 21 and monthly_salary >= 50000 and good_credit_score == "yes":
    print("Loan Approved")
else:
    print("Loan Rejected")