"""
Problem: Calculate Triangle Area from User Input

Description:
Write a Python program that asks the user to enter the base and height of a triangle. Calculate and
display its area.

Formula:
Area = (Base × Height) / 2

Expected Interaction:
Enter base: 10.5
Enter height: 8
Triangle Area: 42.00
"""

base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = (base * height) / 2

print(f"Triangle Area: {area:.2f}")