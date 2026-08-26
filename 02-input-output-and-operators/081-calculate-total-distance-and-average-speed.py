"""
Problem: Calculate Total Distance and Average Speed

Description:
Write a Python program that asks the user to enter the distance travelled, time travelled, and fuel
consumed. Calculate and display the average speed and fuel efficiency.

Formulas:
Average Speed = Distance / Time
Fuel Efficiency = Distance / Fuel Consumed

Expected Interaction:
Enter distance travelled (km): 240
Enter time travelled (hours): 4
Enter fuel consumed (liters): 15

Average Speed: 60.00 km/h
Fuel Efficiency: 16.00 km/L
"""

distance_in_kilometers = float(input("Enter distance travelled (km): "))
time_in_hours = float(input("Enter time travelled (hours): "))
fuel_consumed_in_liters = float(input("Enter fuel consumed (liters): "))

average_speed = distance_in_kilometers / time_in_hours
fuel_efficiency = distance_in_kilometers / fuel_consumed_in_liters

print(f"\nAverage Speed: {average_speed:.2f} km/h")
print(f"Fuel Efficiency: {fuel_efficiency:.2f} km/L")