"""
Problem: Find the Smallest Number in a Sequence

Description:
Find the smallest number among a sequence of numbers entered by the user using a for loop.

Conditions:
- Ask how many numbers the user wants to enter.
- Initialize smallest with the first entered number.
- Compare each remaining number with smallest.
- Update smallest whenever a smaller number is found.
- Display the smallest number.

Expected Interaction:

How many numbers do you want to enter: 5

Enter number 1: 45
Enter number 2: 12
Enter number 3: 67
Enter number 4: 8
Enter number 5: 23

Smallest number: 8
"""

number = int(input("How many numbers do you want to enter: "))

smallest = int(input("Enter number 1: "))

for i in range(2, number + 1):
    num = int(input(f"Enter number {i}: "))

    if num < smallest:
        smallest = num

print(f"\nSmallest number: {smallest}")