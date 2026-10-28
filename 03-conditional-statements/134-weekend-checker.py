"""
Problem: Weekend Checker

Description:
Write a Python program that asks the user to enter a day
of the week. If the day is Saturday or Sunday, display
"It's the Weekend!". Otherwise, display "It's a Weekday.".
The input should be case-insensitive.

Condition:
day == "saturday" or day == "sunday"

Expected Interaction 1:
Enter a day: Saturday

It's the Weekend!

Expected Interaction 2:
Enter a day: Monday

It's a Weekday.
"""

day = input("Enter a day: ").lower()

if day == "saturday" or day == "sunday":
    print("It's the Weekend!")
else:
    print("It's a Weekday.")