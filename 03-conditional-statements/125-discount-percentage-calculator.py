"""
Problem: Discount Percentage Calculator

Description:
Write a Python program that asks the user to enter the total
purchase amount. Determine the discount percentage based on
the purchase amount, then calculate the discount amount and
the final amount after discount.

Discount Rules:
Below 1000       → 0%
1000–4999.99     → 5%
5000–9999.99     → 10%
10000 or above   → 15%

Formulas:
Discount Amount = (Purchase Amount * Discount Percentage) / 100
Final Amount = Purchase Amount - Discount Amount

Expected Interaction:
Enter purchase amount: 6000

Purchase Amount: 6000.00
Discount Percentage: 10%
Discount Amount: 600.00
Final Amount: 5400.00
"""

total_purchase_amount = float(input("Enter purchase amount: "))

if total_purchase_amount < 1000:
    discount_percentage = 0
elif total_purchase_amount < 5000:
    discount_percentage = 5
elif total_purchase_amount < 10000:
    discount_percentage = 10
else:
    discount_percentage = 15

discount_amount = (total_purchase_amount * discount_percentage) / 100
final_amount = total_purchase_amount - discount_amount

print(f"\nPurchase Amount: {total_purchase_amount:.2f}")
print(f"Discount Percentage: {discount_percentage}%")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Amount: {final_amount:.2f}")