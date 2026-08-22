"""
Problem: Calculate Total Bill

Description:
Write a Python program that stores the price of an item, quantity purchased, discount percentage, and
tax percentage in separate variables.

The program should:
1. Calculate the subtotal.
2. Calculate the discount amount.
3. Calculate the price after discount.
4. Calculate the tax amount.
5. Calculate the final bill amount.

Formulas:
Subtotal = Price × Quantity
Discount Amount = (Subtotal × Discount Percentage) / 100
Price After Discount = Subtotal - Discount Amount
Tax Amount = (Price After Discount × Tax Percentage) / 100
Final Bill = Price After Discount + Tax Amount

Expected Output:
Subtotal: 2000
Discount Amount: 200.0
Price After Discount: 1800.0
Tax Amount: 270.0
Final Bill: 2070.0
"""

price = 1000
quantity = 2
discount_percentage = 10
tax_percentage = 15

subtotal = price * quantity

discount_amount = (subtotal * discount_percentage) / 100

price_after_discount = subtotal - discount_amount

tax_amount = (price_after_discount * tax_percentage) / 100

final_bill_amount = price_after_discount + tax_amount

print(f"Subtotal: {subtotal}")
print(f"Discount Amount: {discount_amount}")
print(f"Price After Discount: {price_after_discount}")
print(f"Tax Amount: {tax_amount}")
print(f"Final Bill: {final_bill_amount}")