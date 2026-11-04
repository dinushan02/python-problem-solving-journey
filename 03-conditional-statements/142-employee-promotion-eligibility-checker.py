"""
Problem: Employee Promotion Eligibility Checker

Description:
Determine whether an employee qualifies for a promotion
based on years of experience and performance rating.

Conditions:
- Experience must be greater than or equal to 3 years.
- Performance rating must be greater than or equal to 8.
- Both conditions must be satisfied.

Expected Interaction:

Enter years of experience: 5
Enter performance rating: 9
Eligible for Promotion

Enter years of experience: 2
Enter performance rating: 9
Not Eligible for Promotion
"""

experience_years = int(input("Enter years of experience: "))
performance_rating = int(input("Enter performance rating: "))

if experience_years >= 3 and performance_rating >= 8:
    print("Eligible for Promotion")
else:
    print("Not Eligible for Promotion")