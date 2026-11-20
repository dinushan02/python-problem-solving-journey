"""
Problem: Count Numbers Equal to the Average

Description:
Accept multiple numbers from the user, calculate
their average, and count how many numbers are
equal to the average.

Conditions:
- Ask how many numbers the user wants to enter.
- The number of values must be greater than zero.
- Store all entered numbers in a list.
- Calculate the total and average.
- Use another for loop to compare each number.
- Count numbers equal to the average.
- Display the average and count.

Expected Interaction:

How many numbers do you want to enter: 5

Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50

Average: 30.0
Numbers equal to average: 1
"""

number = int(input("How many numbers do you want to enter: "))

if number > 0:
    numbers = []
    total = 0

    for i in range(1, number + 1):
        num = int(input(f"Enter number {i}: "))

        numbers.append(num)
        total += num

    average = total / len(numbers)

    count = 0

    for i in numbers:
        if average == i:
            count += 1

    print(f"\nAverage: {average}")
    print(f"Numbers equal to average: {count}")

else:
    print("\nPlease enter a positive number of values.")