"""
Problem: Job Application Eligibility Checker

Description:
Determine whether a candidate qualifies for a job
application based on age, education, and work experience.

Conditions:
- Candidate must be at least 18 years old.
- Candidate must have a degree OR work experience.
- Both the age requirement and at least one qualification
  requirement must be satisfied.

Expected Interaction:

Enter your age: 25
Do you have a degree: yes
Do you have work experience: no
Eligible for Job Application

Enter your age: 17
Do you have a degree: yes
Do you have work experience: yes
Not Eligible for Job Application
"""

age = int(input("Enter your age: "))
degree = input("Do you have a degree: ").lower()
work_experience = input("Do you have work experience: ").lower()

if age >= 18 and (degree == "yes" or work_experience == "yes"):
    print("Eligible for Job Application")
else:
    print("Not Eligible for Job Application")