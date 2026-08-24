"""
Problem: Calculate Total Price After Discount

Description:
Write a Python program that asks the user to enter the price per item, quantity purchased, and discount
percentage. Calculate and display the subtotal, discount amount, and final price after applying the discount.

Formulas:
Subtotal = Price × Quantity
Discount Amount = (Subtotal × Discount Percentage) / 100
Final Price = Subtotal - Discount Amount

Expected Interaction:
Enter price per item: 500
Enter quantity: 4
Enter discount percentage: 10
Subtotal: 2000.00
Discount Amount: 200.00
Final Price: 1800.00
"""

price_per_item = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

subtotal = price_per_item * quantity
discount_amount = (subtotal * discount_percentage) / 100
final_price = subtotal - discount_amount

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Price: {final_price:.2f}")