"""
Problem: Online Shopping Free Delivery Checker

Description:
Determine whether a customer qualifies for free delivery
based on their purchase amount or premium membership.

Conditions:
- Purchase amount must be greater than or equal to 5000.
- OR the customer must have premium membership.
- At least one condition must be satisfied.

Expected Interaction:

Enter purchase amount: 6000
Do you have premium membership: yes
Free Delivery Available

Enter purchase amount: 2000
Do you have premium membership: yes
Free Delivery Available

Enter purchase amount: 3000
Do you have premium membership: no
Delivery Charge Applies
"""

total_purchase_amount = float(input("Enter purchase amount: "))
premium_membership = input("Do you have premium membership: ").lower()

if total_purchase_amount >= 5000 or premium_membership == "yes":
    print("Free Delivery Available")
else:
    print("Delivery Charge Applies")