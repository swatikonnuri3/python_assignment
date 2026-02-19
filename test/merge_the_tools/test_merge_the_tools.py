import unittest
from src.merge_the_tools.util import merge_the_tools

class test_merge_the_tools(unittest.TestCase):
    def test_names_case(self):
        result = merge_the_tools("LAKSHMANANPALANIAPPAN", 4)
        self.assertEqual(result, ["LAKS", "HMAN", "ANP","LANI","AP","N"])
    def test_small_groups(self):
        result = merge_the_tools("Leo", 2)
        self.assertEqual(result, ["Le", "o"])
    def test_all_duplicates(self):
        result = merge_the_tools("AAAABBBB", 2)
        self.assertEqual(result, ["A", "A", "B", "B"])
if __name__ == "__main__":
    unittest.main()