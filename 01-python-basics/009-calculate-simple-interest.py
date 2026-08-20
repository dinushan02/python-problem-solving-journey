"""
Problem: Calculate Simple Interest

Description:
Write a Python program that stores the principal amount, rate of interest, and 
time in separate variables, calculates the simple interest, and displays the result.

Formula:
Simple Interest = (Principal × Rate × Time) / 100

Expected Output:
Simple Interest: 1000.0
"""

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: {simple_interest}")