"""
Lambda Functions
Python also supports lambda functions, which are used for writing simple, one-line expressions.
They are also known as anonymous functions because they don’t need a name to be defined. Lambda functions are
especially useful when you need to pass a simple function as an argument to another function, like in the map(),
filter(), or reduce() functions.
"""

add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8

"""
Function Parameters and Return Values
Function parameters are variables defined in the function’s declaration. They receive values when the function is 
called and are used within the function’s code block.

Types of Parameters
Positional Parameters: Parameters passed based on their position in the function call.
Keyword Parameters: Parameters passed with their corresponding variable names.
Default Parameters: Parameters with predefined default values.
Variable-length Parameters: Parameters that can accept a variable number of arguments.
"""

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

# Passing argument
print(calculate_area(10, 5))  # rectangle_area will be 50

"""
Keyword Arguments

When we talk about “passing arguments by name using keyword arguments,” we are referring to a way of giving values to 
functions. Now, let’s talk about keyword arguments. Instead of relying on the position of arguments, you can explicitly 
specify which parameter should take which value by using keywords (parameter names) when calling the function. This 
approach can be helpful when dealing with functions that have many parameters, as it makes the code more readable and 
less error-prone by explicitly stating what each value represents.
"""


def user_info(name, age=None):
    """Prints user information."""
    print(f"Name: {name}")
    if age:
     print(f"Age: {age}")
user_info(name="Bob", age=30)

"""
Default Values
Parameters can have default values assigned within the function definition
"""

# Function definition with default value
def greet(name="World"):
     """Prints a greeting message."""
     print(f"Hello, {name}!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!

"""
Return Values
Return values are the values that a function sends back to the caller after execution. They are specified using the 
return statement in Python. Python functions can return multiple values as a tuple or other iterable types.
"""


def square(number):
 """Returns the square of a number."""
 return number * number
squared_value = square(4)  # squared_value will be 16


my_number= []
def numbers(num1,num2,num3):
    my_number.append(num1)
    my_number.append(num2)
    my_number.append(num3)
    return  my_number

print(numbers(3,4,6))


"""
Variable Scope and Functions

Local vs Global Scope
Variables defined within a function have a local scope, meaning they are only accessible within the function body. 
Variables defined outside functions have a global scope, accessible throughout the program.
"""

count = 0  # Global variable
def increment(count):
    count += 1  # This refers to the local count within the function

increment(4)
print(count)  # Output: 0 (Global count remains unchanged)

"""
global and nonlocal Keywords
Use the global keyword to modify a global variable from within a function
"""

count = 0
def increment_global():
  global count
  count += 1
increment_global()
print(count)  # Output: 1 (Global count is modified)



"""
Use the nonlocal keyword to modify a variable from an enclosing function within a nested function. Let’s break down 
the concept of using the nonlocal keyword to modify a variable from an enclosing function within a nested function in
simpler terms. First, let’s understand what nested functions and enclosing functions are: *Nested Function: This is 
a function defined within another function. *Enclosing Function: This is the outer function that contains the nested
function. Now, when you have a nested function inside an enclosing function, by default, the nested function can 
access variables from the enclosing function, but it cannot modify them directly. However, using the nonlocal 
keyword allows us to modify these variables indirectly.
"""

def outer_function():
    x = 10  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()













