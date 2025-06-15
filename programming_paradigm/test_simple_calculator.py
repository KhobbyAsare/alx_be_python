import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(-1, -1), -2)  # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Zeros

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Negative and positive
        self.assertEqual(self.calc.subtract(-1, -1), 0)  # Negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Zeros

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.multiply(-1, -1), 1)  # Negative numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Zero multiplication

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.divide(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.divide(-4, -2), 2)  # Negative numbers
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero division by non-zero
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

if __name__ == '__main__':
    unittest.main()
