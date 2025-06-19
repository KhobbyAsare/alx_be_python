"""

try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Code that executes if no exception occurs
finally:
  # Code that always executes, regardless of exceptions

...................................

# try block: Contains the code that might potentially raise an exception.

# except block: Catches specific exceptions based on the ExceptionType. You can have multiple except blocks to
handle different exception types.

# else block: Executes code only if no exceptions occur within the try block.

# finally block: Executes code regardless of whether an exception occurs or not. It’s commonly used for
cleaning up resources like closing files.

"""



try:
    f = open("text_content.txt")
except FileNotFoundError:
    # to catch error on file not found
    print("No such file or directory")
except Exception as error:
    # to catch all error instances
    print(error)
else:
    # Executes code only if no exceptions occur within the try block.
    print(f.read())
    f.close()
finally:
    # more of clean up and closing
    print("Program Completed")


# Custom Exception - raise Exception


print("..............Custom Exception...........")

try:
    file = open("text_content.txt")
    raise Exception
except Exception as error:
    print("I raised a custom error")



# Example Sample......................................


class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}



def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("banana", 2)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output:
