"""
Problem: Student Scholarship Eligibility Checker

Description:
Determine whether a student qualifies for a scholarship
based on examination marks and annual family income.

Conditions:
- Examination mark must be greater than or equal to 80.
- Annual family income must be less than or equal to 500000.
- Both conditions must be satisfied.

Expected Interaction:

Enter examination mark: 90
Enter annual family income: 400000
Eligible for Scholarship

Enter examination mark: 85
Enter annual family income: 600000
Not Eligible for Scholarship
"""

examination_mark = float(input("Enter examination mark: "))
annual_family_income = float(input("Enter annual family income: "))

if examination_mark >= 80 and annual_family_income <= 500000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")