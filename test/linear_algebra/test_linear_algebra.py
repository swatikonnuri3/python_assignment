import unittest
from src.linear_algebra.util import lin_alg


class test_lin_alg(unittest.TestCase):
    def test_2x2_matrix(self):
        result = lin_alg(2, [[1, 2], [3, 4]])
        self.assertEqual(result, -2.0)

    def test_3x3_matrix(self):
        result = lin_alg(3, [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]])
        self.assertEqual(result, 1.0)

    def test_4x4_matrix(self):
        result = lin_alg(4, [[2, 0, 0, 0],
                             [0, 2, 0, 0],
                             [0, 0, 2, 0],
                             [0, 0, 0, 2]])
        self.assertEqual(result, 16.0)


if __name__ == "__main__":
    unittest.main()