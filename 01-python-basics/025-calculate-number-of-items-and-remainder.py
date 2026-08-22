"""
Problem: Calculate Number of Items and Remainder

Description:
Write a Python program that stores the total number of items and the number of items 
per box in separate variables.

The program should calculate:
- The number of complete boxes.
- The number of remaining items.

The program should use:
- Integer division (//) to calculate complete boxes.
- Modulus (%) to calculate remaining items.

Expected Output:
Complete Boxes: 4
Remaining Items: 7
"""

total_items = 47
items_per_box = 10

complete_boxes = total_items // items_per_box
remaining_items = total_items % items_per_box

print(f"Complete Boxes: {complete_boxes}")
print(f"Remaining Items: {remaining_items}")