"""
Problem: Calculate Final Price with Tax from User Input

Description:
Write a Python program that asks the user to enter the price and tax percentage. Calculate the 
tax amount and the final price including tax.

Formulas:
Tax Amount = (Price × Tax Percentage) / 100
Final Price = Price + Tax Amount

Expected Interaction:
Enter price: 2000
Enter tax percentage: 15
Tax Amount: 300.0
Final Price: 2300.0
"""

price = float(input("Enter price: "))
tax_percentage = float(input("Enter tax percentage: "))

tax_amount = (price * tax_percentage) / 100
final_price = price + tax_amount

print(f"Tax Amount: {tax_amount}")
print(f"Final Price: {final_price}")