"""
Problem: BMI Category Checker

Description:
Write a Python program that asks the user to enter their
weight in kilograms and height in meters. Calculate their
BMI and display the corresponding category.

Formula:
BMI = Weight (kg) / Height (m) ** 2

Categories:
Below 18.5       → Underweight
18.5–24.9        → Normal Weight
25–29.9          → Overweight
30 or above      → Obesity

Expected Interaction:
Enter weight in kilograms: 70
Enter height in meters: 1.75

BMI: 22.86
Category: Normal Weight
"""

weight_kg = float(input("Enter weight in kilograms: "))
height_m = float(input("Enter height in meters: "))

bmi = weight_kg / height_m ** 2

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"\nBMI: {bmi:.2f}")
print(f"Category: {category}")