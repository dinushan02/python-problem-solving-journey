"""
Problem: Calculate Rental Cost

Description:
Write a Python program that asks the user to enter the daily rental rate, number of days, and insurance
charge per day. Calculate and display the rental cost, insurance cost, and total rental cost.

Formulas:
Rental Cost = Daily Rental Rate × Number of Days
Insurance Cost = Insurance Charge Per Day × Number of Days
Total Rental Cost = Rental Cost + Insurance Cost

Expected Interaction:
Enter daily rental rate: 2500
Enter number of days: 4
Enter insurance charge per day: 500

Rental Cost: 10000.00
Insurance Cost: 2000.00
Total Rental Cost: 12000.00
"""

daily_rental_rate = float(input("Enter daily rental rate: "))
number_of_days = int(input("Enter number of days: "))
insurance_charge_per_day = float(input("Enter insurance charge per day: "))

rental_cost = daily_rental_rate * number_of_days
insurance_cost = insurance_charge_per_day * number_of_days
total_rental_cost = rental_cost + insurance_cost

print(f"\nRental Cost: {rental_cost:.2f}")
print(f"Insurance Cost: {insurance_cost:.2f}")
print(f"Total Rental Cost: {total_rental_cost:.2f}")