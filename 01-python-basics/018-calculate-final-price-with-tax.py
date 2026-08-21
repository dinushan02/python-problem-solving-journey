"""
Problem: Calculate Final Price with Tax

Description:
Write a Python program that stores the price of a product and a tax percentage in 
separate variables. Calculate the tax amount and the final price including tax.

Formula:
Tax Amount = (Price × Tax Percentage) / 100
Final Price = Price + Tax Amount

Expected Output:
Tax Amount: 300.0
Final Price: 2300.0
"""

price = 2000
tax_percentage = 15

tax_amount = (price * tax_percentage) / 100
final_price = price + tax_amount

print(f"Tax Amount: {tax_amount}")
print(f"Final Price: {final_price}")