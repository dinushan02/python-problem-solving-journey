"""
Problem: Count Even Numbers from 1 to N

Description:
Count how many even numbers exist between 1 and a number entered by the user using a for loop.

Conditions:
- Initialize count with 0.
- Iterate from 1 to the entered number.
- Check whether each number is even.
- Increase count by 1 whenever an even number is found.
- Display the final count.

Expected Interaction:

Enter a number: 10

Count of even numbers from 1 to 10: 5
"""

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        count += 1

print(f"\nCount of even numbers from 1 to {num}: {count}")