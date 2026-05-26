import unittest

from calculator.core import CalculatorError, add, apply, divide, multiply, subtract


class TestCore(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(CalculatorError):
            divide(1, 0)

    def test_apply(self):
        self.assertEqual(apply(6, "+", 2), 8)
        self.assertEqual(apply(6, "-", 2), 4)
        self.assertEqual(apply(6, "*", 2), 12)
        self.assertEqual(apply(6, "/", 2), 3)


if __name__ == "__main__":
    unittest.main()
