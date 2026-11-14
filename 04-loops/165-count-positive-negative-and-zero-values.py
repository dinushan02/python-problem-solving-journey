"""
Problem: Count Positive, Negative, and Zero Values

Description:
Accept multiple numbers from the user and count how
many are positive, negative, and equal to zero.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Initialize three counters with 0.
- Use a for loop to accept each number.
- Classify each number as positive, negative, or zero.
- Increase the appropriate counter.
- Display all three counts.

Expected Interaction:

How many numbers do you want to enter: 6

Enter number 1: 10
Enter number 2: -5
Enter number 3: 0
Enter number 4: 20
Enter number 5: -8
Enter number 6: 0

Positive numbers: 2
Negative numbers: 2
Zero numbers: 2
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))

        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(f"\nPositive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zero numbers: {zero_count}")

else:
    print("\nPlease enter a positive number of values.")