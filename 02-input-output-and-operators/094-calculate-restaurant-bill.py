"""
Problem: Calculate Restaurant Bill

Description:
Write a Python program that asks the user to enter the food cost, beverage cost, and service charge
percentage. Calculate and display the subtotal, service charge, and final bill.

Formulas:
Subtotal = Food Cost + Beverage Cost
Service Charge = (Subtotal × Service Charge Percentage) / 100
Final Bill = Subtotal + Service Charge

Expected Interaction:
Enter food cost: 2500
Enter beverage cost: 1000
Enter service charge percentage: 10

Subtotal: 3500.00
Service Charge: 350.00
Final Bill: 3850.00
"""

food_cost = float(input("Enter food cost: "))
beverage_cost = float(input("Enter beverage cost: "))
service_charge_percentage = float(input("Enter service charge percentage: "))

subtotal = food_cost + beverage_cost
service_charge = (subtotal * service_charge_percentage) / 100
final_bill = subtotal + service_charge

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Service Charge: {service_charge:.2f}")
print(f"Final Bill: {final_bill:.2f}")