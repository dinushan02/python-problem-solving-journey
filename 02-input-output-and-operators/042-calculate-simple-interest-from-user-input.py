"""
Problem: Calculate Simple Interest from User Input

Description:
Write a Python program that asks the user to enter the principal amount, rate of interest, 
and time in years. Calculate and display the simple interest.

Formula:
Simple Interest = (Principal × Rate × Time) / 100

Expected Interaction:
Enter principal: 10000
Enter rate: 5
Enter time in years: 2
Simple Interest: 1000.0
"""

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time_in_years = float(input("Enter time in years: "))

interest = (principal * rate * time_in_years) / 100

print(f"Simple Interest: {interest}")