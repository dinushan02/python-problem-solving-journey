"""
Problem: Calculate Shopping Cart with Discount and Tax

Description:
Write a Python program that asks the user to enter the price of a product, quantity, discount percentage,
and tax percentage. Calculate and display the subtotal, discount amount, price after discount, tax amount, and final bill.

Formulas:
Subtotal = Price × Quantity
Discount Amount = (Subtotal × Discount Percentage) / 100
Price After Discount = Subtotal - Discount Amount
Tax Amount = (Price After Discount × Tax Percentage) / 100
Final Bill = Price After Discount + Tax Amount

Expected Interaction:
Enter price of product: 2500
Enter quantity: 3
Enter discount percentage: 10
Enter tax percentage: 15

Subtotal: 7500.00
Discount Amount: 750.00
Price After Discount: 6750.00
Tax Amount: 1012.50
Final Bill: 7762.50
"""

product_price = float(input("Enter price of product: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))
tax_percentage = float(input("Enter tax percentage: "))

subtotal = product_price * quantity
discount_amount = (subtotal * discount_percentage) / 100
price_after_discount = subtotal - discount_amount
tax_amount = (price_after_discount * tax_percentage) / 100
final_bill = price_after_discount + tax_amount

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Price After Discount: {price_after_discount:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Bill: {final_bill:.2f}")