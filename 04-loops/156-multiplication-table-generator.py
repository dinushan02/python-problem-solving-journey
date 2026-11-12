"""
Problem: Multiplication Table Generator

Description:
Generate the multiplication table of a number entered by the user from 1 to 10.

Conditions:
- Accept an integer from the user.
- Use a for loop to generate the table.
- Multiply the entered number by each value from 1 to 10.
- Display each multiplication with its result.

Expected Interaction:

Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

