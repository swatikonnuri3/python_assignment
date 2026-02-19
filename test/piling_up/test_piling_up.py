import unittest
from src.piling_up.util import pile_up

class test_pile_up(unittest.TestCase):
    def test_yes_case(self):
        cubes = [4, 3, 2, 1, 3, 4]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_no_case(self):
        cubes = [1, 3, 2]
        self.assertEqual(pile_up(cubes), "No")

    def test_equal(self):
        cubes = [5, 5, 5, 5]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_desc(self):
        cubes = [6, 5, 4, 3, 2, 1]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_asc(self):
        cubes = [1, 2, 3, 4, 5]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_one(self):
        cubes = [7]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_two_yes(self):
        cubes = [3, 2]
        self.assertEqual(pile_up(cubes), "Yes")

    def test_two_no(self):
        cubes = [2, 3]
        self.assertEqual(pile_up(cubes), "Yes")

if __name__ == "__main__":
    unittest.main()