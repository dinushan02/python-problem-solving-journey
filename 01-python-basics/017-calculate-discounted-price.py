"""
Problem: Calculate Discounted Price

Description:
Write a Python program that stores the original price of a product and a discount percentage in 
separate variables. Calculate the discount amount and the final price after applying the discount.

Formula:
Discount Amount = (Price × Discount Percentage) / 100
Final Price = Price - Discount Amount

Expected Output:
Discount Amount: 100.0
Final Price: 900.0
"""

price = 1000
discount_percentage = 10

discount_amount = price * (discount_percentage / 100)

final_price = price - discount_amount

print(f"Discount Amount: {discount_amount}")
print(f"Final Price: {final_price}")