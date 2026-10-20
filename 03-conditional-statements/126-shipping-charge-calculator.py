"""
Problem: Shipping Charge Calculator

Description:
Write a Python program that asks the user to enter the total
order amount. Calculate the shipping charge according to the
order amount, then display the order amount, shipping charge,
and final amount including shipping.

Shipping Rules:
Below 1000       → Shipping Charge: 150
Below 5000     → Shipping Charge: 75
5000 or above    → Free Shipping

Formula:
Final Amount = Order Amount + Shipping Charge

Expected Interaction:
Enter order amount: 3000

Order Amount: 3000.00
Shipping Charge: 75.00
Final Amount: 3075.00
"""

total_order_amount = float(input("Enter order amount: "))

if total_order_amount < 1000:
    shipping_charge = 150
elif total_order_amount < 5000:
    shipping_charge = 75
else:
    shipping_charge = 0

final_amount = total_order_amount + shipping_charge

print(f"\nOrder Amount: {total_order_amount:.2f}")
print(f"Shipping Charge: {shipping_charge:.2f}")
print(f"Final Amount: {final_amount:.2f}")