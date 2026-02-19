import unittest
from src.mean_var_std.util import mean_var_std

class test_mean_var_std(unittest.TestCase):
    def test_2x2_matrix(self):
        matrix = [[1, 2],
                  [3, 4]]
        mean, var, std = mean_var_std(2, 2, matrix)
        self.assertAlmostEqual(mean[0], 1.5, places=3)
        self.assertAlmostEqual(mean[1], 3.5, places=3)
        self.assertAlmostEqual(var[0], 1.0, places=3)
        self.assertAlmostEqual(var[1], 1.0, places=3)
        self.assertAlmostEqual(std, 1.118, places=3)
    def test_3x3_identity(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        mean, var, std = mean_var_std(3, 3, matrix)
        self.assertAlmostEqual(mean[0], 0.333, places=3)
        self.assertAlmostEqual(mean[1], 0.333, places=3)
        self.assertAlmostEqual(mean[2], 0.333, places=3)
        self.assertAlmostEqual(var[0], 0.222, places=3)
        self.assertAlmostEqual(var[1], 0.222, places=3)
        self.assertAlmostEqual(var[2], 0.222, places=3)
        self.assertAlmostEqual(std, 0.471, places=3)

if __name__ == "__main__":
    unittest.main()