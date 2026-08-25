"""
Problem: Calculate Total Shopping Cart with Discount

Description:
Write a Python program that asks the user to enter the price and quantity of three different products, then asks for a discount percentage. 
Calculate and display each product total, subtotal, discount amount, and final price.

Formulas:
Product Total = Price × Quantity
Subtotal = Product 1 Total + Product 2 Total + Product 3 Total
Discount Amount = (Subtotal × Discount Percentage) / 100
Final Price = Subtotal - Discount Amount

Expected Interaction:
Enter price of product 1: 500
Enter quantity of product 1: 2

Enter price of product 2: 250
Enter quantity of product 2: 3

Enter price of product 3: 1000
Enter quantity of product 3: 1

Enter discount percentage: 10

Product 1 Total: 1000.00
Product 2 Total: 750.00
Product 3 Total: 1000.00
Subtotal: 2750.00
Discount Amount: 275.00
Final Price: 2475.00
"""

price_product1 = float(input("Enter price of product 1: "))
quantity_product1 = int(input("Enter quantity of product 1: "))

price_product2 = float(input("\nEnter price of product 2: "))
quantity_product2 = int(input("Enter quantity of product 2: "))

price_product3 = float(input("\nEnter price of product 3: "))
quantity_product3 = int(input("Enter quantity of product 3: "))

discount_percentage = float(input("\nEnter discount percentage: "))

total_cost_product1 = price_product1 * quantity_product1
total_cost_product2 = price_product2 * quantity_product2
total_cost_product3 = price_product3 * quantity_product3

subtotal = total_cost_product1 + total_cost_product2 + total_cost_product3
discount_amount = (subtotal * discount_percentage) / 100
final_price = subtotal - discount_amount

print(f"\nProduct 1 Total: {total_cost_product1:.2f}")
print(f"Product 2 Total: {total_cost_product2:.2f}")
print(f"Product 3 Total: {total_cost_product3:.2f}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Price: {final_price:.2f}")