import unittest
from src.find_the_runner_up.util import second_max

class test_second_max(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(second_max([10, 20, 30]), 20)

    def test_with_duplicates(self):
        self.assertEqual(second_max([5, 5, 10, 10, 20]), 10)

    def test_all_same(self):
        self.assertIsNone(second_max([7, 7, 7]))

    def test_single_element(self):
        self.assertIsNone(second_max([42]))

    def test_negative_numbers(self):
        self.assertEqual(second_max([-10, -20, -30]), -20)

    def test_large_list(self):
        self.assertEqual(second_max([1, 2, 3, 4, 5, 100]), 5)

if __name__ == "__main__":
    unittest.main()