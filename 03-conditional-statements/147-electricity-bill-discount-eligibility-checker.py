"""
Problem: Electricity Bill Discount Eligibility Checker

Description:
Determine whether a household qualifies for an electricity
bill discount based on consumption or senior citizen status.

Conditions:
- Electricity consumption must be less than or equal to 100 units.
- OR the customer must be a senior citizen.
- At least one condition must be satisfied.

Expected Interaction:

Enter electricity consumption: 80
Are you a senior citizen: no
Discount Eligible

Enter electricity consumption: 150
Are you a senior citizen: yes
Discount Eligible

Enter electricity consumption: 200
Are you a senior citizen: no
Discount Not Eligible
"""

electricity_units = int(input("Enter electricity consumption: "))
senior_citizen = input("Are you a senior citizen: ").lower()

if electricity_units <= 100 or senior_citizen == "yes":
    print("Discount Eligible")
else:
    print("Discount Not Eligible")