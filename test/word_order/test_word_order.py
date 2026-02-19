import unittest
from src.word_order.util import find_word_order

class test_word_order(unittest.TestCase):
    def test_one(self):
        words = ["aaa"]
        expected = {"aaa": 1}
        self.assertEqual(find_word_order(1, words), expected)

    def test_repeat(self):
        words = ["bbb", "bbb", "bbb"]
        expected = {"bbb": 3}
        self.assertEqual(find_word_order(3, words), expected)

    def test_two(self):
        words = ["aaa", "bbb"]
        expected = {"aaa": 1, "bbb": 1}
        self.assertEqual(find_word_order(2, words), expected)

    def test_mix(self):
        words = ["aaa", "bbb", "aaa", "ccc", "bbb"]
        expected = {"aaa": 2, "bbb": 2, "ccc": 1}
        self.assertEqual(find_word_order(5, words), expected)

    def test_empty(self):
        words = []
        expected = {}
        self.assertEqual(find_word_order(0, words), expected)

if __name__ == "__main__":
    unittest.main()