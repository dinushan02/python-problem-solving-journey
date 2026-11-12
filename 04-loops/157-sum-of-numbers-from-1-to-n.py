"""
Problem: Sum of Numbers from 1 to N

Description:
Calculate the sum of all numbers from 1 to a number entered by the user using a for loop.

Conditions:
- Initialize total with 0.
- Iterate from 1 to the entered number.
- Add each number to the accumulator.
- Display the final sum.

Expected Interaction:

Enter a number: 5

Sum of numbers from 1 to 5: 15
"""

num = int(input("Enter a number: "))

total = 0

for i in range(1, num + 1):
    total += i

print(f"\nSum of numbers from 1 to {num}: {total}")