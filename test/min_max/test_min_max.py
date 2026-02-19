import unittest
from src.min_max.util import min_max

class test_min_max(unittest.TestCase):
    def test_2x2_matrix(self):
        matrix = [[1, 2],
                  [3, 4]]
        result = min_max(2, 2, matrix)
        self.assertEqual(result, 3)
    def test_3x3_matrix(self):
        matrix = [[7, 8, 9],
                  [4, 5, 6],
                  [1, 2, 3]]
        result = min_max(3, 3, matrix)
        self.assertEqual(result, 7)
    def test_with_duplicates(self):
        matrix = [[5, 5],
                  [5, 5]]
        result = min_max(2, 2, matrix)
        self.assertEqual(result, 5)
if __name__ == "__main__":
    unittest.main()