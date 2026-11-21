"""
Problem: Count Duplicate Numbers in a List

Description:
Accept multiple numbers from the user and identify
how many distinct values appear more than once.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all numbers in a list.
- Create an empty duplicates list.
- Use numbers.count() to identify repeated values.
- Add each duplicate value only once.
- Count the distinct duplicate values.
- Display the duplicate values and their count.

Expected Interaction:

How many numbers do you want to enter: 7

Enter number 1: 10
Enter number 2: 20
Enter number 3: 10
Enter number 4: 30
Enter number 5: 20
Enter number 6: 40
Enter number 7: 10

Duplicate numbers: [10, 20]
Total distinct duplicate numbers: 2
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    duplicates = []
    duplicates_count = 0

    for num in numbers:
        if numbers.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)
                duplicates_count += 1

    print(f"\nDuplicate numbers: {duplicates}")
    print(f"Total distinct duplicate numbers: {duplicates_count}")

else:
    print("\nPlease enter a positive number of values.")