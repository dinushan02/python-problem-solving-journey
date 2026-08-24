"""
Problem: Calculate Total Distance Travelled

Description:
Write a Python program that asks the user to enter the average speed in kilometers per hour and the
time travelled in hours. Calculate and display the total distance travelled in kilometers.

Formula:
Distance = Speed × Time

Expected Interaction:
Enter average speed in km/h: 60
Enter time travelled in hours: 2.5
Total Distance: 150.00 km
"""

average_speed_in_kilometers_per_hour = float(input("Enter average speed in km/h: "))
time_travelled_in_hours = float(input("Enter time travelled in hours: "))

total_distance = average_speed_in_kilometers_per_hour * time_travelled_in_hours

print(f"Total Distance: {total_distance:.2f} km")