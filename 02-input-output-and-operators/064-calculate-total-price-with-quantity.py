"""
Problem: Calculate Total Price with Quantity

Description:
Write a Python program that asks the user to enter the price per item and quantity purchased. Calculate
and display the total price.

Formula:
Total Price = Price × Quantity

Expected Interaction:
Enter price per item: 250.50
Enter quantity: 4
Total Price: 1002.00
"""

price_per_item = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

total_price = price_per_item * quantity

print(f"Total Price: {total_price:.2f}")