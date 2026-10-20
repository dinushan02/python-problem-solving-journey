"""
Problem: Leap Year Checker

Description:
Write a Python program that asks the user to enter a year.
Determine whether the year is a leap year using the standard
Gregorian calendar rules.

Rules:
1. Divisible by 400 → Leap Year
2. Otherwise, divisible by 100 → Not a Leap Year
3. Otherwise, divisible by 4 → Leap Year
4. Otherwise → Not a Leap Year

Expected Interaction 1:
Enter a year: 2024

Leap Year

Expected Interaction 2:
Enter a year: 1900

Not a Leap Year

Expected Interaction 3:
Enter a year: 2000

Leap Year
"""

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")