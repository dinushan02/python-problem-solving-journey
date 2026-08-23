"""
Problem: Calculate Discounted Price from User Input

Description:
Write a Python program that asks the user to enter the original price and discount percentage. 
Calculate the discount amount and the final price after applying the discount.

Formulas:
Discount Amount = (Price × Discount Percentage) / 100
Final Price = Price - Discount Amount

Expected Interaction:
Enter price: 2500
Enter discount percentage: 10
Discount Amount: 250.0
Final Price: 2250.0
"""

price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_amount = (price * discount_percentage) / 100
final_price = price - discount_amount

print(f"Discount Amount: {discount_amount}")
print(f"Final Price: {final_price}")