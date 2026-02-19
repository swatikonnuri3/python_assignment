from src.calendar_module.util import get_day
import unittest

class calendar_test(unittest.TestCase):

    def test_get_day(self):
        self.assertEqual(get_day(4, 12, 2004), "SATURDAY")

    def test_leap_year(self):
        self.assertEqual(get_day(29,2, 2021), "SATURDAY")

    def test_new_year(self):
        self.assertEqual(get_day(1, 1, 2026), "THURSDAY")

    def test_end_of_year(self):
        self.assertEqual(get_day(31,12, 2025), "WEDNESDAY")

    def test_recent_date(self):
        self.assertEqual(get_day(18,2, 2024), "WEDNESDAY")

if __name__ == "__main__":
    unittest.main()