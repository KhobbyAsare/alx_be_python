"""
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that
supports addition, subtraction, multiplication, and division operations.

Provided: simple_calculator.py
You’re given a SimpleCalculator class with basic arithmetic operations. Your task is to write unit tests
to verify its correctness.
"""

# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b