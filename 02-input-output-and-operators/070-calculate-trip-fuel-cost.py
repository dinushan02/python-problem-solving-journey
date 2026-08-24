"""
Problem: Calculate Trip Fuel Cost

Description:
Write a Python program that asks the user to enter the trip distance, vehicle mileage, and fuel price
per liter. Calculate and display the fuel needed and total fuel cost.

Formulas:
Fuel Needed = Distance / Mileage
Fuel Cost = Fuel Needed × Fuel Price

Expected Interaction:
Enter trip distance (km): 240
Enter vehicle mileage (km/L): 16
Enter fuel price per liter: 320

Fuel Needed: 15.00 L
Total Fuel Cost: 4800.00
"""

trip_distance_km = float(input("Enter trip distance (km): "))
vehicle_mileage_in_km_per_liter = float(input("Enter vehicle mileage (km/L): "))
fuel_price_per_liter = float(input("Enter fuel price per liter: "))

fuel_needed = trip_distance_km / vehicle_mileage_in_km_per_liter
total_fuel_cost = fuel_needed * fuel_price_per_liter

print(f"\nFuel Needed: {fuel_needed:.2f} L")
print(f"Total Fuel Cost: {total_fuel_cost:.2f}")