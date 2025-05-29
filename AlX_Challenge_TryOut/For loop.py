from itertools import count

fruits = ["apple", "orange", "banana"] # List

# for fruit in fruits:
#     print(fruit)

colors = ("red", "green", "blue") # Tuple

# for color in colors:
#     print(color)


# range loop

# for attempt in range(5):
#     print(f"Attempted {attempt}")

# for number in range(1,5):  #start and end number
#     print(f"Attempted {number}")

# for number in range(1,10,2):  #start, end and step or intervals
#     print(f"Attempted {number}")

# For_Else Loop
successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 time and failed")


# Nested Loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")


print("ITERABLE OBJECTS")
# 1. range()
# range returns a range object which is iterable that is why we can iterate over a range
# print(type(range(3))) <class 'range'>

# 2. string
# for x in "Python":
#     print(x)

# 3. List
for x in fruits:
    print(x)

# Exercise 1
count_num = 0
for x in range(1,10):
    if x % 2 == 0:
        count_num += 1
        print(x)
print(f"We have {count_num} even numbers")



"""
Challenge
Numbers can add up quickly! Write a Python program using a for loop to calculate the sum of all the numbers in a list.

Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
Initialize a variable total to 0, which will store the running sum.
Use a for loop to iterate over the numbers list.
Inside the loop, add the current number (use the loop variable) to the total variable.
After the loop, print the final total value, which represents the sum of all the numbers in the list.
"""

numbers = [1, 5, 3, 9]

total = 0

for number in numbers:
    total += number
print(f"Total for the numbers: {total}")