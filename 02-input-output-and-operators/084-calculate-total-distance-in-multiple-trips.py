"""
Problem: Calculate Total Distance in Multiple Trips

Description:
Write a Python program that asks the user to enter the distance travelled for three different trips.
Calculate and display the total distance travelled and the average distance per trip.

Formulas:
Total Distance = Trip 1 + Trip 2 + Trip 3
Average Distance = Total Distance / 3

Expected Interaction:
Enter distance for trip 1 (km): 120
Enter distance for trip 2 (km): 180
Enter distance for trip 3 (km): 150

Total Distance: 450.00 km
Average Distance Per Trip: 150.00 km
"""

trip1_distance_km = float(input("Enter distance for trip 1 (km): "))
trip2_distance_km = float(input("Enter distance for trip 2 (km): "))
trip3_distance_km = float(input("Enter distance for trip 3 (km): "))

total_distance_travelled = (
    trip1_distance_km
    + trip2_distance_km
    + trip3_distance_km
)

average_distance_per_trip = total_distance_travelled / 3

print(f"\nTotal Distance: {total_distance_travelled:.2f} km")
print(f"Average Distance Per Trip: {average_distance_per_trip:.2f} km")