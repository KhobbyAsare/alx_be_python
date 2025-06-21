"""
Note for you:

Understand the use of @staticmethod for functions that perform a task in isolation, without needing access
to class or instance-specific data.

Grasp the concept of @classmethod for functions that need to access class attributes or methods and understand
how the cls parameter allows access to class-level attributes.

This task underscores the distinction between class methods and static methods in Python, providing
clarity on their appropriate use cases and advantages.

"""

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b