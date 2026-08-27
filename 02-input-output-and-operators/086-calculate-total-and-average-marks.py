"""
Problem: Calculate Total and Average Marks

Description:
Write a Python program that asks the user to enter the marks obtained in five subjects. Calculate and
display the total marks and average marks.

Formulas:
Total Marks = Subject 1 + Subject 2 + Subject 3 + Subject 4 + Subject 5
Average Marks = Total Marks / 5

Expected Interaction:
Enter marks for subject 1: 80
Enter marks for subject 2: 75
Enter marks for subject 3: 90
Enter marks for subject 4: 85
Enter marks for subject 5: 70

Total Marks: 400.00
Average Marks: 80.00
"""

subject1_marks = float(input("Enter marks for subject 1: "))
subject2_marks = float(input("Enter marks for subject 2: "))
subject3_marks = float(input("Enter marks for subject 3: "))
subject4_marks = float(input("Enter marks for subject 4: "))
subject5_marks = float(input("Enter marks for subject 5: "))

total_marks = (
    subject1_marks
    + subject2_marks
    + subject3_marks
    + subject4_marks
    + subject5_marks
)

average_marks = total_marks / 5

print(f"\nTotal Marks: {total_marks:.2f}")
print(f"Average Marks: {average_marks:.2f}")