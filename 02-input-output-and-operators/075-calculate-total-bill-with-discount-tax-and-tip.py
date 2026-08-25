"""
Problem: Calculate Total Bill with Discount, Tax, and Tip

Description:
Write a Python program that asks the user to enter the bill amount, discount percentage, tax percentage, and tip percentage. 
Calculate and display the discount amount, price after discount, tax amount, tip amount, and final bill.

Formulas:
Discount Amount = (Bill × Discount Percentage) / 100
Price After Discount = Bill - Discount Amount
Tax Amount = (Price After Discount × Tax Percentage) / 100
Tip Amount = (Price After Discount × Tip Percentage) / 100
Final Bill = Price After Discount + Tax Amount + Tip Amount

Expected Interaction:
Enter bill amount: 5000
Enter discount percentage: 10
Enter tax percentage: 15
Enter tip percentage: 5

Discount Amount: 500.00
Price After Discount: 4500.00
Tax Amount: 675.00
Tip Amount: 225.00
Final Bill: 5400.00
"""

bill_amount = float(input("Enter bill amount: "))
discount_percentage = float(input("Enter discount percentage: "))
tax_percentage = float(input("Enter tax percentage: "))
tip_percentage = float(input("Enter tip percentage: "))

discount_amount = (bill_amount * discount_percentage) / 100
price_after_discount = bill_amount - discount_amount
tax_amount = (price_after_discount * tax_percentage) / 100
tip_amount = (price_after_discount * tip_percentage) / 100
final_bill = price_after_discount + tax_amount + tip_amount

print(f"\nDiscount Amount: {discount_amount:.2f}")
print(f"Price After Discount: {price_after_discount:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Tip Amount: {tip_amount:.2f}")
print(f"Final Bill: {final_bill:.2f}")