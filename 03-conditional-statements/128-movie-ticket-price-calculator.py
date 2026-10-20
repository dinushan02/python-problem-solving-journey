"""
Problem: Movie Ticket Price Calculator

Description:
Write a Python program that asks the user to enter their age.
Determine their age category and movie ticket price based on
the following rules.

Ticket Rules:
Below 5       → Free
5–12          → Child, 5.00
13–59         → Adult, 10.00
60 or above   → Senior, 7.00

Expected Interaction 1:
Enter your age: 25

Age Category: Adult
Ticket Price: 10.00

Expected Interaction 2:
Enter your age: 8

Age Category: Child
Ticket Price: 5.00

Expected Interaction 3:
Enter your age: 65

Age Category: Senior
Ticket Price: 7.00
"""

age = int(input("Enter your age: "))

if age < 5:
    age_category = "Child"
    ticket_price = 0
elif 5 <= age <= 12:
    age_category = "Child"
    ticket_price = 5.00
elif 13 <= age <= 59:
    age_category = "Adult"
    ticket_price = 10.00
else:
    age_category = "Senior"
    ticket_price = 7.00

print(f"\nAge Category: {age_category}")
print(f"Ticket Price: {ticket_price:.2f}")