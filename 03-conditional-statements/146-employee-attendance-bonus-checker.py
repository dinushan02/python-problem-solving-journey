"""
Problem: Employee Attendance Bonus Checker

Description:
Determine whether an employee qualifies for an attendance
bonus based on attendance percentage and disciplinary history.

Formula:
Attendance Percentage = (Days Attended / Total Working Days) * 100

Conditions:
- Attendance percentage must be greater than or equal to 95%.
- Employee must have no disciplinary warning.
- Both conditions must be satisfied.

Expected Interaction:

Enter total working days: 100
Enter days attended: 98
Any disciplinary warning: no
Eligible for Attendance Bonus

Enter total working days: 100
Enter days attended: 90
Any disciplinary warning: no
Not Eligible for Attendance Bonus
"""

total_working_days = int(input("Enter total working days: "))
days_attended = int(input("Enter days attended: "))
disciplinary_warning = input("Any disciplinary warning: ").lower()

attendance_percentage = (days_attended * 100) / total_working_days

if attendance_percentage >= 95 and disciplinary_warning == "no":
    print("Eligible for Attendance Bonus")
else:
    print("Not Eligible for Attendance Bonus")