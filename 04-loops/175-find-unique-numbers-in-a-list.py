"""
Problem: Find Unique Numbers in a List

Description:
Accept multiple numbers from the user and identify
the numbers that appear exactly once.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all numbers in a list.
- Create an empty unique_numbers list.
- Use numbers.count() to check each number's frequency.
- Add numbers that appear exactly once.
- Count the unique numbers.
- Display the unique numbers and their count.

Expected Interaction:

How many numbers do you want to enter: 7

Enter number 1: 10
Enter number 2: 20
Enter number 3: 10
Enter number 4: 30
Enter number 5: 40
Enter number 6: 20
Enter number 7: 50

Unique numbers: [30, 40, 50]
Total unique numbers: 3
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    unique_numbers = []
    unique_numbers_count = 0

    for num in numbers:
        if numbers.count(num) == 1:
            if num not in unique_numbers:
                unique_numbers.append(num)
                unique_numbers_count += 1

    print(f"\nUnique numbers: {unique_numbers}")
    print(f"Total unique numbers: {unique_numbers_count}")

else:
    print("\nPlease enter a positive number of values.")