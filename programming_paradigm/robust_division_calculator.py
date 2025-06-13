"""
Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling,
and main.py, which interfaces with the user through the command line.

"""

def safe_divide(numerator, denominator) ->  str:
    try:
        # Attempt to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."