"""
Problem: Calculate Total Bill with Tip

Description:
Write a Python program that asks the user to enter the bill amount and tip percentage. Calculate the
tip amount and the total bill including the tip.

Formulas:
Tip Amount = (Bill Amount × Tip Percentage) / 100
Total Bill = Bill Amount + Tip Amount

Expected Interaction:
Enter bill amount: 2000
Enter tip percentage: 10
Tip Amount: 200.00
Total Bill: 2200.00
"""

bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = (bill_amount * tip_percentage) / 100
total_bill = bill_amount + tip_amount

print(f"Tip Amount: {tip_amount:.2f}")
print(f"Total Bill: {total_bill:.2f}")