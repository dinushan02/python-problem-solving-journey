"""
Problem: Shopping Cart Discount Calculator

Description:
Calculate a shopping discount based on the purchase amount
and premium membership status.

Conditions:
- Purchase amount >= 10000 AND premium membership:
  20% discount.
- Purchase amount >= 10000 OR premium membership:
  10% discount.
- Neither condition:
  0% discount.

Formulas:
Discount Amount = (Purchase Amount * Discount Percentage) / 100
Final Amount = Purchase Amount - Discount Amount

Expected Interaction:

Enter purchase amount: 12000
Do you have premium membership: yes

Purchase Amount: 12000.00
Discount Percentage: 20%
Discount Amount: 2400.00
Final Amount: 9600.00

Enter purchase amount: 12000
Do you have premium membership: no

Purchase Amount: 12000.00
Discount Percentage: 10%
Discount Amount: 1200.00
Final Amount: 10800.00
"""

purchase_amount = float(input("Enter purchase amount: "))
premium_membership = input("Do you have premium membership: ").lower()

if purchase_amount >= 10000 and premium_membership == "yes":
    discount_percentage = 20
elif purchase_amount >= 10000 or premium_membership == "yes":
    discount_percentage = 10
else:
    discount_percentage = 0

discount_amount = (purchase_amount * discount_percentage) / 100
final_amount = purchase_amount - discount_amount

print(f"\nPurchase Amount: {purchase_amount:.2f}")
print(f"Discount Percentage: {discount_percentage}%")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Amount: {final_amount:.2f}")