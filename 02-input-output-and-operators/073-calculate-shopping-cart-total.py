"""
Problem: Calculate Shopping Cart Total

Description:
Write a Python program that asks the user to enter the price and quantity of three different products.
Calculate and display the total cost of each product and the grand total.

Formulas:
Product Total = Price × Quantity
Grand Total = Product 1 Total + Product 2 Total + Product 3 Total

Expected Interaction:
Enter price of product 1: 500
Enter quantity of product 1: 2

Enter price of product 2: 250
Enter quantity of product 2: 3

Enter price of product 3: 1000
Enter quantity of product 3: 1

Product 1 Total: 1000.00
Product 2 Total: 750.00
Product 3 Total: 1000.00
Grand Total: 2750.00
"""

price_product1 = float(input("Enter price of product 1: "))
quantity_product1 = int(input("Enter quantity of product 1: "))

price_product2 = float(input("\nEnter price of product 2: "))
quantity_product2 = int(input("Enter quantity of product 2: "))

price_product3 = float(input("\nEnter price of product 3: "))
quantity_product3 = int(input("Enter quantity of product 3: "))

total_cost_product1 = price_product1 * quantity_product1
total_cost_product2 = price_product2 * quantity_product2
total_cost_product3 = price_product3 * quantity_product3

grand_total = total_cost_product1 + total_cost_product2 + total_cost_product3

print(f"\nProduct 1 Total: {total_cost_product1:.2f}")
print(f"Product 2 Total: {total_cost_product2:.2f}")
print(f"Product 3 Total: {total_cost_product3:.2f}")
print(f"Grand Total: {grand_total:.2f}")