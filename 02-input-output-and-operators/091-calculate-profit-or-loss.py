"""
Problem: Calculate Profit or Loss

Description:
Write a Python program that asks the user to enter the cost price and selling price. Calculate and display
the profit or loss amount and profit or loss percentage.

Formula:
Profit/Loss Amount = Selling Price - Cost Price
Profit/Loss Percentage = (Profit/Loss Amount / Cost Price) × 100

Expected Interaction:
Enter cost price: 5000
Enter selling price: 6000

Profit/Loss Amount: 1000.00
Profit/Loss Percentage: 20.00%
"""

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

profit_or_loss_amount = selling_price - cost_price
profit_or_loss_percentage = (profit_or_loss_amount / cost_price) * 100

print(f"\nProfit/Loss Amount: {profit_or_loss_amount:.2f}")
print(f"Profit/Loss Percentage: {profit_or_loss_percentage:.2f}%")