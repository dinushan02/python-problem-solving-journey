"""
Problem: Calculate Average Speed

Description:
Write a Python program that asks the user to enter the distance travelled in kilometers and the time
taken in hours. Calculate and display the average speed in kilometers per hour.

Formula:
Average Speed = Distance / Time

Expected Interaction:
Enter distance in kilometers: 150
Enter time in hours: 3
Average Speed: 50.00 km/h
"""

distance_in_kilometers = float(input("Enter distance in kilometers: "))
time_in_hours = float(input("Enter time in hours: "))

average_speed = distance_in_kilometers / time_in_hours

print(f"Average Speed: {average_speed:.2f} km/h")