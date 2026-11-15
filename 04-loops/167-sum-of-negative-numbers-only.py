"""
Problem: Sum of Negative Numbers Only

Description:
Accept multiple numbers from the user and calculate
the sum of only negative numbers using a for loop.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Initialize negative_total with 0.
- Use a for loop to accept each number.
- Add only numbers less than zero.
- Display the final sum.

Expected Interaction:

How many numbers do you want to enter: 6

Enter number 1: 10
Enter number 2: -5
Enter number 3: 0
Enter number 4: -20
Enter number 5: 8
Enter number 6: -15

Sum of negative numbers: -40
"""

number = int(input("How many numbers do you want to enter: "))

negative_total = 0

if number > 0:
    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))

        if num < 0:
            negative_total += num

    print(f"\nSum of negative numbers: {negative_total}")

else:
    print("\nPlease enter a positive number of values.")