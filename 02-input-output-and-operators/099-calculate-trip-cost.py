"""
Problem: Calculate Trip Cost

Description:
Write a Python program that asks the user to enter the trip distance, vehicle mileage, fuel price per liter,
accommodation cost, and food cost. Calculate and display the fuel required, fuel cost, and total trip cost.

Formulas:
Fuel Required = Trip Distance / Vehicle Mileage
Fuel Cost = Fuel Required × Fuel Price Per Liter
Total Trip Cost = Fuel Cost + Accommodation Cost + Food Cost

Expected Interaction:
Enter trip distance (km): 500
Enter vehicle mileage (km/L): 15
Enter fuel price per liter: 350
Enter accommodation cost: 10000
Enter food cost: 5000

Fuel Required: 33.33 L
Fuel Cost: 11666.67
Total Trip Cost: 26666.67
"""

trip_distance_kilometers = float(input("Enter trip distance (km): "))
vehicle_mileage_km_l = float(input("Enter vehicle mileage (km/L): "))
fuel_price_per_liter = float(input("Enter fuel price per liter: "))
accommodation_cost = float(input("Enter accommodation cost: "))
food_cost = float(input("Enter food cost: "))

fuel_required = trip_distance_kilometers / vehicle_mileage_km_l
fuel_cost = fuel_required * fuel_price_per_liter
total_trip_cost = fuel_cost + accommodation_cost + food_cost

print(f"\nFuel Required: {fuel_required:.2f} L")
print(f"Fuel Cost: {fuel_cost:.2f}")
print(f"Total Trip Cost: {total_trip_cost:.2f}")