"""
Problem: Calculate Electricity Bill

Description:
Write a Python program that asks the user to enter the units consumed, cost per unit, and fixed service
charge. Calculate and display the energy cost and total electricity bill.

Formulas:
Energy Cost = Units Consumed × Cost Per Unit
Total Bill = Energy Cost + Fixed Service Charge

Expected Interaction:
Enter units consumed: 250
Enter cost per unit: 12.50
Enter fixed service charge: 500

Energy Cost: 3125.00
Total Electricity Bill: 3625.00
"""

units_consumed = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))
fixed_service_charge = float(input("Enter fixed service charge: "))

energy_cost = units_consumed * cost_per_unit
total_electricity_bill = energy_cost + fixed_service_charge

print(f"\nEnergy Cost: {energy_cost:.2f}")
print(f"Total Electricity Bill: {total_electricity_bill:.2f}")