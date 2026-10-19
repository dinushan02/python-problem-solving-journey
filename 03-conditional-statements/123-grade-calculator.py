"""
Problem: Grade Calculator

Description:
Write a Python program that asks the user to enter an exam mark.
Determine the grade based on the following ranges:

90–100 → Grade A
80–89  → Grade B
70–79  → Grade C
60–69  → Grade D
Below 60 → Grade F

Assumption:
The entered mark is an integer between 0 and 100.

Conditions:
Grade A → 90 <= mark <= 100
Grade B → 80 <= mark <= 89
Grade C → 70 <= mark <= 79
Grade D → 60 <= mark <= 69
Grade F → Otherwise

Expected Interaction 1:
Enter your mark: 95

Grade: A

Expected Interaction 2:
Enter your mark: 84

Grade: B

Expected Interaction 3:
Enter your mark: 55

Grade: F
"""

mark = int(input("Enter your mark: "))

if 90 <= mark <= 100:
    print("Grade: A")
elif 80 <= mark <= 89:
    print("Grade: B")
elif 70 <= mark <= 79:
    print("Grade: C")
elif 60 <= mark <= 69:
    print("Grade: D")
else:
    print("Grade: F")