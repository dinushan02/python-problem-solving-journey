"""
Problem: Calculate Total and Remaining Money

Description:
Write a Python program that asks the user to enter the total money available and the amount spent.
Calculate and display the remaining money and the percentage of money spent.

Formulas:
Remaining Money = Total Money - Amount Spent
Percentage Spent = (Amount Spent / Total Money) × 100

Expected Interaction:
Enter total money: 10000
Enter amount spent: 3500
Remaining Money: 6500.00
Percentage Spent: 35.00%
"""

total_money = float(input("Enter total money: "))
amount_spent = float(input("Enter amount spent: "))

remaining_money = total_money - amount_spent
percentage_spent = (amount_spent / total_money) * 100

print(f"Remaining Money: {remaining_money:.2f}")
print(f"Percentage Spent: {percentage_spent:.2f}%")