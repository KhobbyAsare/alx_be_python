"""
**Exercise 1**: Handling`ZeroDivisionError`

Instructions:

- Write a program that takes two numbers as input from the user and divides the first number by the second number.
- Handle the`ZeroDivisionError`exception to inform the user if they attempt to divide by zero.
"""

def division():
    numb1 = float(input("Enter your first digit to be divided: "))
    num2 = float(input("Enter the next digit to divide with: "))

    try:
        if num2 == 0:
            raise ZeroDivisionError
    except ZeroDivisionError as error:
        print(f"Error: you attempted to divide by zero {error}")
    else:
        print(f"Result: {numb1 / num2}")


division()


"""
Exercise 2: File Handling with FileNotFoundError

Instructions:

Write a program that attempts to open and read data from a file specified by the user.
Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.
"""

print("")
print(".........File Handling..........")
print("")

def fileHandling():
    try:
        f = open("text_content.txt")
    except FileNotFoundError as fileError:
        print(fileError)
    except Exception as error:
        print(error)
    else:
        print(f.read())
        f.close()
    finally:
        print("File programme completed....")


fileHandling()


"""
Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.
"""


# Define the custom exception class
class ValueTooHighError(Exception):
    """Raised when the input value is too high"""
    pass

def handleValueTooHighError():
    try:
        # Get input from the user
        getValue = float(input("Guess the value: "))

        # Check if the value is too high
        if getValue > 100:
            raise ValueTooHighError
        else:
            print("The value is acceptable.")
    except ValueTooHighError:
        print("ValueTooHighError: The value is too high.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function to test it
handleValueTooHighError()


