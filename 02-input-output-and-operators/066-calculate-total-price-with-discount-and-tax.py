"""
Problem: Calculate Total Price with Discount and Tax

Description:
Write a Python program that asks the user to enter the price per item, quantity purchased, discount percentage, 
and tax percentage. Calculate and display the subtotal, discount amount, price after discount, tax amount, and final price.

Formulas:
Subtotal = Price × Quantity
Discount Amount = (Subtotal × Discount Percentage) / 100
Price After Discount = Subtotal - Discount Amount
Tax Amount = (Price After Discount × Tax Percentage) / 100
Final Price = Price After Discount + Tax Amount

Expected Interaction:
Enter price per item: 1000
Enter quantity: 2
Enter discount percentage: 10
Enter tax percentage: 15

Subtotal: 2000.00
Discount Amount: 200.00
Price After Discount: 1800.00
Tax Amount: 270.00
Final Price: 2070.00
"""

price_per_item = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))
tax_percentage = float(input("Enter tax percentage: "))

subtotal = price_per_item * quantity
discount_amount = (subtotal * discount_percentage) / 100
price_after_discount = subtotal - discount_amount
tax_amount = (price_after_discount * tax_percentage) / 100
final_price = price_after_discount + tax_amount

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Price After Discount: {price_after_discount:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Price: {final_price:.2f}")