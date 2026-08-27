"""
Problem: Calculate Total Cost Per Person

Description:
Write a Python program that asks the user to enter the total bill amount, number of people, and tip
percentage. Calculate and display the tip amount, total bill including the tip, and amount each person should pay.

Formulas:
Tip Amount = (Total Bill × Tip Percentage) / 100
Total Bill = Total Bill + Tip Amount
Amount Per Person = Total Bill / Number of People

Expected Interaction:
Enter total bill amount: 6000
Enter number of people: 4
Enter tip percentage: 10

Tip Amount: 600.00
Total Bill: 6600.00
Amount Per Person: 1650.00
"""

total_bill_amount = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = (total_bill_amount * tip_percentage) / 100
total_bill_with_tip = total_bill_amount + tip_amount
amount_per_person = total_bill_with_tip / number_of_people

print(f"\nTip Amount: {tip_amount:.2f}")
print(f"Total Bill: {total_bill_with_tip:.2f}")
print(f"Amount Per Person: {amount_per_person:.2f}")