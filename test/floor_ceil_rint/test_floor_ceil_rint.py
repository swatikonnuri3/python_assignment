import unittest
import numpy
from src.floor_ceil_rint.util import print_fcr

class test_fcr(unittest.TestCase):
    def test_array_with_decimals(self):
        A = numpy.array([1.2, 2.5, 3.7], float)
        floor, ceil, rint = print_fcr(A)
        self.assertTrue(numpy.array_equal(floor, [1., 2., 3.]))
        self.assertTrue(numpy.array_equal(ceil, [2., 3., 4.]))
        self.assertTrue(numpy.array_equal(rint, [1., 2., 4.]))

    def test_array_with_integers(self):
        A = numpy.array([1, 2, 3], float)
        floor, ceil, rint = print_fcr(A)
        self.assertTrue(numpy.array_equal(floor, [1., 2., 3.]))
        self.assertTrue(numpy.array_equal(ceil, [1., 2., 3.]))
        self.assertTrue(numpy.array_equal(rint, [1., 2., 3.]))

    def test_array_with_negatives(self):
        A = numpy.array([-1.2, -2.5, -3.7], float)
        floor, ceil, rint = print_fcr(A)
        self.assertTrue(numpy.array_equal(floor, [-2., -3., -4.]))
        self.assertTrue(numpy.array_equal(ceil, [-1., -2., -3.]))
        self.assertTrue(numpy.array_equal(rint, [-1., -2., -4.]))

if __name__ == "__main__":
    unittest.main()