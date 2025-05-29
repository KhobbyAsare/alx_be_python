# 1. User Input Validation:
# age = 0
#
# while age < 18:
#   age = int(input("Enter your age (must be 18 or older): "))
#
# print("You are old enough to proceed.")

# 2. Guessing Game:
# secret_number = 7
#
# guess_count = 0
# guess = 0
#
# while guess != secret_number:
#   guess_count += 1
#   guess = int(input("Guess a number between 1 and 10: "))
#
# print(f"You guessed it in {guess_count} tries!")

# 3. Iterating Until a Specific Condition:
# shopping_list = ["apples", "bread", "milk", "cheese"]
# item_found = False
#
# while not item_found:
#   item = input("Search for an item in your list (or 'q' to quit): ")
#   if item.lower() == "q":
#     break  # Exit the loop if user enters 'q'
#   if item in shopping_list:
#     item_found = True
#     print(f"{item} is on your shopping list.")
#   else:
#     print(f"{item} is not on your list.")

# Example: Printing a Multiplication Table
#
# for i in range(1, 11):
#   # Outer loop iterates through rows (multiplication factors)
#   for j in range(1, 11):
#     # Inner loop iterates through columns (other factors)
#     product = i * j
#     print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
#   print()  # Move to a new line after each row


# Printing a Right Triangle of Asterisks

# rows = 5

# for i in range(1, rows + 1):
#   # Outer loop controls the number of rows
#   for j in range(1, i + 1):
#     # Inner loop prints asterisks for each row
#     print("*", end="")
#   print()  # Move to a new line after each row of asterisks

rows = 5
i = 1  # Start from row 1

while i <= rows:
    # Print spaces
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1

    # Print stars
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()  # Move to the next line
    i += 1
