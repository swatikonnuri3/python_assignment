import unittest
from src.mutations.util import mutate_string

class test_mutation(unittest.TestCase):
    def test_middle_change(self):
        result = mutate_string("Lakshmanan", 4, "X")
        self.assertEqual(result, "LaksXmanan")

    def test_first_change(self):
        result = mutate_string("Walter", 0, "S")
        self.assertEqual(result, "Salter")

    def test_last_change(self):
        result = mutate_string("Jessy", 4, "Z")
        self.assertEqual(result, "JessZ")

if __name__ == "__main__":
    unittest.main()