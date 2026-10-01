"""
Problem: Calculate Complete Order Bill

Description:
Write a Python program that asks the user to enter the product price, quantity, discount percentage,
tax percentage, and shipping charge. Calculate and display the subtotal, discount amount, price after
discount, tax amount, price after tax, and final order bill including shipping.

Formulas:
Subtotal = Product Price × Quantity
Discount Amount = (Subtotal × Discount Percentage) / 100
Price After Discount = Subtotal - Discount Amount
Tax Amount = (Price After Discount × Tax Percentage) / 100
Price After Tax = Price After Discount + Tax Amount
Final Order Bill = Price After Tax + Shipping Charge

Expected Interaction:
Enter product price: 2500
Enter quantity: 3
Enter discount percentage: 10
Enter tax percentage: 15
Enter shipping charge: 500

Subtotal: 7500.00
Discount Amount: 750.00
Price After Discount: 6750.00
Tax Amount: 1012.50
Price After Tax: 7762.50
Final Order Bill: 8262.50
"""

product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))
tax_percentage = float(input("Enter tax percentage: "))
shipping_charge = float(input("Enter shipping charge: "))

subtotal = product_price * quantity
discount_amount = (subtotal * discount_percentage) / 100
price_after_discount = subtotal - discount_amount
tax_amount = (price_after_discount * tax_percentage) / 100
price_after_tax = price_after_discount + tax_amount
final_bill_with_shipping = price_after_tax + shipping_charge

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Price After Discount: {price_after_discount:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Price After Tax: {price_after_tax:.2f}")
print(f"Final Order Bill: {final_bill_with_shipping:.2f}")