"""
Problem: Swap Two Variables

Description:
Write a Python program that stores two numbers in two separate variables and swaps their values.

Expected Output:
Before swapping:
a = 10
b = 20

After swapping:
a = 20
b = 10
"""

a = 10
b = 20

print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

print("\nAfter swapping:")
print(f"a = {a}")
print(f"b = {b}")