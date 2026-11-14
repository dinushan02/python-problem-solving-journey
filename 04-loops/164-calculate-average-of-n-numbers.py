"""
Problem: Calculate the Average of N Numbers

Description:
Calculate the average of a sequence of numbers entered by the user using a for loop.

Formula:
Average = Total / Number of Values

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Initialize total with 0.
- Use a for loop to accept each number.
- Add each number to total.
- Calculate and display the average.

Expected Interaction:

How many numbers do you want to enter: 5
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50

Average: 30.0
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    total = 0

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        total += num

    average = total / number

    print(f"\nAverage: {average}")
else:
    print("\nPlease enter a positive number of values.")