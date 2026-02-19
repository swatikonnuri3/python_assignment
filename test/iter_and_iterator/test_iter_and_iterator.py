import unittest
from src.iter_and_iterator.util import probability_with_a

class test_iter_and_iterator(unittest.TestCase):
    def test_basic_case(self):
        result = probability_with_a(4, ["a", "b", "c", "d"], 2)
        self.assertAlmostEqual(result, 0.5)

    def test_all_a(self):
        result = probability_with_a(3, ["a", "a", "a"], 2)
        self.assertAlmostEqual(result, 1.0)

    def test_no_a(self):
        result = probability_with_a(3, ["b", "c", "d"], 2)
        self.assertAlmostEqual(result, 0.0)

    def test_multiple_a(self):
        result = probability_with_a(4, ["a", "a", "b", "c"], 2)
        self.assertAlmostEqual(result, 0.8333333333, places=6)

    def test_mismatched_length(self):
        with self.assertRaises(ValueError):
            probability_with_a(4, ["a", "a", "a", "a", "a"], 2)

if __name__ == "__main__":
    unittest.main()