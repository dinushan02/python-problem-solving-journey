"""
Problem: Calculate Speed and Travel Time

Description:
Write a Python program that asks the user to enter the distance in kilometers and average speed in km/h.
Calculate and display the travel time in hours and minutes.

Formulas:
Travel Time (hours) = Distance / Speed
Travel Time (minutes) = Travel Time (hours) × 60

Expected Interaction:
Enter distance (km): 240
Enter average speed (km/h): 60

Travel Time: 4.00 hours
Travel Time: 240.00 minutes
"""

distance_km = float(input("Enter distance (km): "))
average_speed_km_h = float(input("Enter average speed (km/h): "))

travel_time_in_hours = distance_km / average_speed_km_h
travel_time_in_minutes = travel_time_in_hours * 60

print(f"\nTravel Time: {travel_time_in_hours:.2f} hours")
print(f"Travel Time: {travel_time_in_minutes:.2f} minutes")