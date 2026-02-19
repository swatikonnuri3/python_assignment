import unittest
from src.time_delta.util import time_delta

class test_time_delta(unittest.TestCase):
    def test_same_time(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0700"
        self.assertEqual(time_delta(t1, t2), "0")
    def test_one_hour_diff(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 14:54:36 -0700"
        self.assertEqual(time_delta(t1, t2), "3600")
    def test_timezone_diff(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "88200")
    def test_day_diff(self):
        t1 = "Mon 11 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0700"
        self.assertEqual(time_delta(t1, t2), "86400")
if __name__ == "__main__":
    unittest.main()