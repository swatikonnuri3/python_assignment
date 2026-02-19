import unittest
from src.list_operations.util import list_operations

class test_list_op(unittest.TestCase):
    def test_insert(self):
        result = list_operations([], "insert", 0, 5)
        self.assertEqual(result, [5])

    def test_append(self):
        result = list_operations([], "append", 10)
        self.assertEqual(result, [10])

    def test_remove(self):
        result = list_operations([1, 2, 3], "remove", 2)
        self.assertEqual(result, [1, 3])

    def test_sort(self):
        result = list_operations([3, 1, 2], "sort")
        self.assertEqual(result, [1, 2, 3])

    def test_pop(self):
        result = list_operations([1, 2, 3], "pop")
        self.assertEqual(result, [1, 2])

    def test_reverse(self):
        result = list_operations([1, 2, 3], "reverse")
        self.assertEqual(result, [3, 2, 1])

if __name__ == "__main__":
    unittest.main()