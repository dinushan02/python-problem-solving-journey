"""
Problem: Print Even Numbers from 1 to 20

Description:
Use a for loop and conditional statement to print
all even numbers between 1 and 20.

Conditions:
- Iterate through numbers from 1 to 20.
- Check whether each number is divisible by 2.
- Print only even numbers.

Expected Interaction:

2
4
6
8
10
12
14
16
18
20
"""

for num in range(1, 21):
    if num % 2 == 0:
        print(num)