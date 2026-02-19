import unittest
from src.string_formatting.util import print_formatted
class test_print_fmt(unittest.TestCase):
    def test_one(self):
        self.assertEqual(print_formatted(1), "1 1 1 1")
    def test_two(self):
        self.assertEqual(print_formatted(2), "1 1 1 1\n2 2 2 10")
    def test_three(self):
        self.assertEqual(print_formatted(3), "1 1 1 1\n2 2 2 10\n3 3 3 11")
if __name__ == "__main__":
    unittest.main()