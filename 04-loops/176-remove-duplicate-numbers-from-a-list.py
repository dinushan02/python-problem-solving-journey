"""
Problem: Remove Duplicate Numbers from a List

Description:
Accept multiple numbers from the user and create
a new list containing only distinct numbers while
preserving their original order.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all numbers in a list.
- Create an empty unique_numbers list.
- Iterate through the original list.
- Add a number only if it is not already present.
- Display the original and updated lists.

Expected Interaction:

How many numbers do you want to enter: 7

Enter number 1: 10
Enter number 2: 20
Enter number 3: 10
Enter number 4: 30
Enter number 5: 20
Enter number 6: 40
Enter number 7: 10

Original list: [10, 20, 10, 30, 20, 40, 10]
List after removing duplicates: [10, 20, 30, 40]
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print(f"\nOriginal list: {numbers}")
    print(f"List after removing duplicates: {unique_numbers}")

else:
    print("\nPlease enter a positive number of values.")