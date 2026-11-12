"""
Problem: Sum of Odd Numbers from 1 to N

Description:
Calculate the sum of all odd numbers between 1 and a number entered by the user using a for loop.

Conditions:
- Initialize total with 0.
- Iterate from 1 to the entered number.
- Check whether each number is odd.
- Add only odd numbers to the accumulator.
- Display the final sum.

Expected Interaction:

Enter a number: 10

Sum of odd numbers from 1 to 10: 25
"""

num = int(input("Enter a number: "))

total = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        total += i

print(f"\nSum of odd numbers from 1 to {num}: {total}")