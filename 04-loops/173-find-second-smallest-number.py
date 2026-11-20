"""
Problem: Find the Second Smallest Number

Description:
Accept multiple numbers from the user and find
the smallest and second-smallest distinct numbers.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all entered numbers in a list.
- Find the smallest number.
- Find the smallest number strictly greater than the smallest.
- If no second-smallest distinct number exists,
  display an appropriate message.

Expected Interaction:

How many numbers do you want to enter: 6

Enter number 1: 45
Enter number 2: 12
Enter number 3: 67
Enter number 4: 8
Enter number 5: 23
Enter number 6: 15

Smallest number: 8
Second smallest number: 12
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    smallest_number = numbers[0]

    for num in numbers:
        if num < smallest_number:
            smallest_number = num

    second_smallest_number = None

    for num in numbers:
        if num > smallest_number:
            if second_smallest_number is None or num < second_smallest_number:
                second_smallest_number = num

    print(f"\nSmallest number: {smallest_number}")

    if second_smallest_number is not None:
        print(f"Second smallest number: {second_smallest_number}")
    else:
        print("No second-smallest distinct number exists.")

else:
    print("\nPlease enter a positive number of values.")