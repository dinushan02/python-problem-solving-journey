"""
Problem: Calculate Circle Area from User Input

Description:
Write a Python program that asks the user to enter the radius of a circle, calculates its area, 
and displays the result.

Formula:
Area = π × radius²

Assumption:
π = 3.14

Expected Interaction:
Enter radius: 5
Area: 78.5
"""

radius = float(input("Enter radius: "))

area = 3.14 * radius ** 2

print(f"Area: {area}")