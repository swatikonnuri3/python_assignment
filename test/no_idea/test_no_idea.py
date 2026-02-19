import unittest
from src.no_idea.util import calculate_happiness

class test_no_idea(unittest.TestCase):
    def test_liked(self):
        arr = [1, 2, 3]
        set_a = {1, 2, 3}
        set_b = set()
        self.assertEqual(calculate_happiness(arr, set_a, set_b), 3)
    def test_disliked(self):
        arr = [1, 2, 3]
        set_a = set()
        set_b = {1, 2, 3}
        self.assertEqual(calculate_happiness(arr, set_a, set_b), -3)
    def test_mix(self):
        arr = [1, 2, 3, 4]
        set_a = {1, 4}
        set_b = {2}
        self.assertEqual(calculate_happiness(arr, set_a, set_b), 1)
    def test_none(self):
        arr = [5, 6, 7]
        set_a = {1, 2}
        set_b = {3, 4}
        self.assertEqual(calculate_happiness(arr, set_a, set_b), 0)
    def test_empty(self):
        arr = []
        set_a = {1, 2}
        set_b = {3, 4}
        self.assertEqual(calculate_happiness(arr, set_a, set_b), 0)
    def test_extra(self):
        arr = [1, 2]
        set_a = {1, 2, 3, 4, 5}
        set_b = {6, 7, 8}
        self.assertEqual(calculate_happiness(arr, set_a, set_b), 2)
if __name__ == "__main__":
    unittest.main()