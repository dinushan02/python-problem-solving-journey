"""
Problem: Calculate Rectangle Area from User Input

Description:
Write a Python program that asks the user to enter the length and width of a rectangle, 
calculates its area, and displays the result.

Formula:
Area = Length × Width

Expected Interaction:
Enter length: 12
Enter width: 5
Area: 60.0
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print(f"Area: {area}")