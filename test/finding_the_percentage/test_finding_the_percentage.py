import unittest
from src.finding_the_percentage.util import find_percentage

class test_find_the_percentage(unittest.TestCase):
    def test_normal_case(self):
        data = {"Leo": [90, 80, 70], "Bob": [85, 95, 100]}
        self.assertAlmostEqual(find_percentage(data, "Leo"), 80.0)

    def test_single_score(self):
        data = {"AAAA": [100]}
        self.assertEqual(find_percentage(data, "AAAA"), 100.0)

    def test_with_floats(self):
        data = {"P1": [75.5, 84.5, 90.0]}
        self.assertAlmostEqual(find_percentage(data, "P1"), 83.33, places=2)

    def test_missing_student(self):
        data = {"Max": [60, 70, 80]}
        with self.assertRaises(ValueError):
            find_percentage(data, "Steve")
if __name__ == "__main__":
    unittest.main()