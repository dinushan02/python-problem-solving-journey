"""
Problem: Calculate Circle Circumference from User Input

Description:
Write a Python program that asks the user to enter the radius of a circle. Calculate and display the
circumference.

Formula:
Circumference = 2 × π × Radius

Assumption:
π = 3.14

Expected Interaction:
Enter radius: 7.5
Circumference: 47.10
"""

radius = float(input("Enter radius: "))

circumference = 2 * 3.14 * radius

print(f"Circumference: {circumference:.2f}")