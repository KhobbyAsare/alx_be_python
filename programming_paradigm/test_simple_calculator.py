import unittest
from simple_calculator import SimpleCalculator


class SimpleCalculator_Test( unittest.TestCase):
    def test_add_positive(self):
        result = SimpleCalculator.add(3, 3)
        self.assertEqual(result, 6)



if __name__ == '__main__':
    unittest.main()