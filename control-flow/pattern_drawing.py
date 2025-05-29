"""
Task Description:

Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer,
then use nested loops to print a square pattern of that size made of asterisks (*).
"""

size = int(input("Enter the size of the pattern: "))

outer_checker = 0

while outer_checker < size:
    inner_check = 0
    while inner_check < size:
        print("*", end="")
        inner_check += 1
    outer_checker += 1
    print()