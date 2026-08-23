"""
Problem: Calculate Percentage

Description:
Write a Python program that asks the user to enter the marks obtained and total marks. 
Calculate and display the percentage.

Formula:
Percentage = (Marks Obtained / Total Marks) × 100

Expected Interaction:
Enter marks obtained: 450
Enter total marks: 500
Percentage: 90.00%
"""

marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

percentage = (marks_obtained / total_marks) * 100

print(f"Percentage: {percentage:.2f}%")