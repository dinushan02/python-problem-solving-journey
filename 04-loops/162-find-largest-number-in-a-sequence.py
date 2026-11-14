"""
Problem: Find the Largest Number in a Sequence

Description:
Find the largest number among a sequence of numbers entered by the user using a for loop.

Conditions:
- Ask how many numbers the user wants to enter.
- Initialize largest with the first entered number.
- Compare each remaining number with largest.
- Update largest whenever a bigger number is found.
- Display the largest number.

Expected Interaction:

How many numbers do you want to enter? 5

Enter number 1: 12
Enter number 2: 45
Enter number 3: 8
Enter number 4: 67
Enter number 5: 23

Largest number: 67
"""

number = int(input("How many numbers do you want to enter: "))

largest = int(input("Enter number 1: "))

for i in range(2, number + 1):
    num = int(input(f"Enter number {i}: "))

    if num > largest:
        largest = num

print(f"\nLargest number: {largest}")