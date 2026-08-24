"""
Problem: Calculate Rectangle Perimeter from User Input

Description:
Write a Python program that asks the user to enter the length and width of a rectangle. Calculate and
display its perimeter.

Formula:
Perimeter = 2 × (Length + Width)

Expected Interaction:
Enter length: 12.5
Enter width: 5.5
Perimeter: 36.00
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)

print(f"Perimeter: {perimeter:.2f}")