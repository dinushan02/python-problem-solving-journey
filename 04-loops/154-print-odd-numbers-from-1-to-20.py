"""
Problem: Print Odd Numbers from 1 to 20

Description:
Use a for loop and conditional statement to print
all odd numbers between 1 and 20.

Conditions:
- Iterate through numbers from 1 to 20.
- Check whether each number is not divisible by 2.
- Print only odd numbers.

Expected Interaction:

1
3
5
7
9
11
13
15
17
19
"""

for num in range(1, 21):
    if num % 2 != 0:
        print(num)