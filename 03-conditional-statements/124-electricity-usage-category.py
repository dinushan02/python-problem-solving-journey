"""
Problem: Electricity Usage Category

Description:
Write a Python program that asks the user to enter their
monthly electricity consumption in units (kWh).
Classify the consumption into one of four categories.

Categories:
0–100 units   → Low Usage
Above 100–300 → Moderate Usage
Above 300–500 → High Usage
Above 500     → Very High Usage

Assumption:
Electricity consumption is a non-negative number.

Expected Interaction 1:
Enter electricity units: 75
Low Usage

Expected Interaction 2:
Enter electricity units: 250
Moderate Usage

Expected Interaction 3:
Enter electricity units: 450
High Usage

Expected Interaction 4:
Enter electricity units: 650
Very High Usage
"""

monthly_electricity_units_kWh = float(input("Enter electricity units: "))

if 0 <= monthly_electricity_units_kWh <= 100:
    print("Low Usage")
elif monthly_electricity_units_kWh <= 300:
    print("Moderate Usage")
elif monthly_electricity_units_kWh <= 500:
    print("High Usage")
elif monthly_electricity_units_kWh > 500:
    print("Very High Usage")