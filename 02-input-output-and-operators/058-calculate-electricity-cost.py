"""
Problem: Calculate Electricity Cost

Description:
Write a Python program that asks the user to enter the units of electricity consumed and the cost per
unit. Calculate and display the total electricity cost.

Formula:
Total Cost = Units Consumed × Cost Per Unit

Expected Interaction:
Enter units of electricity consumed: 250
Enter cost per unit: 12.50
Total Electricity Cost: 3125.00
"""

units_of_electricity_consumed = float(input("Enter units of electricity consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))

total_cost = units_of_electricity_consumed * cost_per_unit

print(f"Total Electricity Cost: {total_cost:.2f}")