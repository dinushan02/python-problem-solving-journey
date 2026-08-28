"""
Problem: Calculate Body Mass Index (BMI)

Description:
Write a Python program that asks the user to enter their weight in kilograms and height in meters.
Calculate and display their Body Mass Index.

Formula:
BMI = Weight / (Height × Height)

Expected Interaction:
Enter weight (kg): 70
Enter height (m): 1.75

BMI: 22.86
"""

weight_kg = float(input("Enter weight (kg): "))
height_m = float(input("Enter height (m): "))

bmi = weight_kg / (height_m * height_m)

print(f"\nBMI: {bmi:.2f}")