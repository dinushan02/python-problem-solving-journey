"""
Problem: Calculate Total Cost

Description:
Write a Python program that stores the price of an item, the quantity purchased, and 
the amount paid in separate variables.

The program should:
- Calculate the total cost.
- Calculate the remaining amount after payment.

Formula:
Total Cost = Price × Quantity
Remaining Amount = Amount Paid - Total Cost

Expected Output:
Total Cost: 1000
Remaining Amount: 200
"""

price = 250
quantity = 4
amount_paid = 1200

total_cost = price * quantity
remaining_amount = amount_paid - total_cost

print(f"Total Cost: {total_cost}")
print(f"Remaining Amount: {remaining_amount}")