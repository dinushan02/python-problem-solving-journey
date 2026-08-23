"""
Problem: Calculate Remaining Balance After Payment

Description:
Write a Python program that asks the user to enter the total balance and payment amount. Calculate and
display the remaining balance after the payment.

Formula:
Remaining Balance = Total Balance - Payment Amount

Expected Interaction:
Enter total balance: 50000
Enter payment amount: 12500
Remaining Balance: 37500.00
"""

total_balance = float(input("Enter total balance: "))
payment_amount = float(input("Enter payment amount: "))

remaining_balance = total_balance - payment_amount

print(f"Remaining Balance: {remaining_balance:.2f}")