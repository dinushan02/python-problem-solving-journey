"""
Problem: Calculate Electricity Bill with Fixed Charge

Description:
Write a Python program that asks the user to enter the electricity units consumed, cost per unit, fixed
service charge, and tax percentage. Calculate and display the energy cost, subtotal, tax amount, and final electricity bill.

Formulas:
Energy Cost = Units Consumed × Cost Per Unit
Subtotal = Energy Cost + Fixed Service Charge
Tax Amount = (Subtotal × Tax Percentage) / 100
Final Bill = Subtotal + Tax Amount

Expected Interaction:
Enter units consumed: 250
Enter cost per unit: 20
Enter fixed service charge: 500
Enter tax percentage: 10

Energy Cost: 5000.00
Subtotal: 5500.00
Tax Amount: 550.00
Final Electricity Bill: 6050.00
"""

electricity_units = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))
fixed_service_charge = float(input("Enter fixed service charge: "))
tax_percentage = float(input("Enter tax percentage: "))

energy_cost = electricity_units * cost_per_unit
subtotal = energy_cost + fixed_service_charge
tax_amount = (subtotal * tax_percentage) / 100
final_bill = subtotal + tax_amount

print(f"\nEnergy Cost: {energy_cost:.2f}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Electricity Bill: {final_bill:.2f}")