"""
Problem: Find the Largest and Smallest Numbers Together

Description:
Accept multiple numbers from the user and find both
the largest and smallest numbers using a for loop.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Initialize largest and smallest using the first number.
- Compare each remaining number with both variables.
- Update largest or smallest when necessary.
- Display both results.

Expected Interaction:

How many numbers do you want to enter: 5

Enter number 1: 45
Enter number 2: 12
Enter number 3: 67
Enter number 4: 8
Enter number 5: 23

Largest number: 67
Smallest number: 8
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    smallest = largest = int(input("Enter number 1: "))

    for i in range(2, number + 1):
        num = int(input(f"Enter number {i}: "))

        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    print(f"\nLargest number: {largest}")
    print(f"Smallest number: {smallest}")

else:
    print("\nPlease enter a positive number of values.")