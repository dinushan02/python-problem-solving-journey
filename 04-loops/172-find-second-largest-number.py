"""
Problem: Find the Second Largest Number

Description:
Accept multiple numbers from the user and find the largest and second-largest distinct numbers.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all entered numbers in a list.
- Find the largest number.
- Find the largest number strictly smaller than the largest.
- If no second-largest distinct number exists,
  display an appropriate message.

Expected Interaction:

How many numbers do you want to enter: 6

Enter number 1: 10
Enter number 2: 45
Enter number 3: 20
Enter number 4: 67
Enter number 5: 30
Enter number 6: 55

Largest number: 67
Second largest number: 55
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    largest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num

    second_largest_number = None

    for num in numbers:
        if num < largest_number:
            if second_largest_number is None or num > second_largest_number:
                second_largest_number = num

    print(f"\nLargest number: {largest_number}")

    if second_largest_number is not None:
        print(f"Second largest number: {second_largest_number}")
    else:
        print("No second-largest distinct number exists.")

else:
    print("\nPlease enter a positive number of values.")