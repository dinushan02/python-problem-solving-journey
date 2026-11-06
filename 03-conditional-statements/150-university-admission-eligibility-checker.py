"""
Problem: University Admission Eligibility Checker

Description:
Determine whether a student qualifies for university
admission based on four examination results.

Conditions:
- Mathematics marks >= 75.
- Science marks >= 70.
- English marks >= 60.
- Entrance examination marks >= 80.
- All four conditions must be satisfied.

Expected Interaction:

Enter Mathematics marks: 85
Enter Science marks: 80
Enter English marks: 75
Enter Entrance examination marks: 90

University Admission: Approved

Enter Mathematics marks: 90
Enter Science marks: 65
Enter English marks: 80
Enter Entrance examination marks: 90

University Admission: Rejected
"""

mathematics_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))
entrance_examination_marks = float(input("Enter Entrance examination marks: "))

if mathematics_marks >= 75 and science_marks >= 70 and english_marks >= 60 and entrance_examination_marks >= 80:
    print("\nUniversity Admission: Approved")
else:
    print("\nUniversity Admission: Rejected")