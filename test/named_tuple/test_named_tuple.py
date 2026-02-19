import unittest
from src.named_tuple.util import named_tuple
class test_named_tuple(unittest.TestCase):
    def test1(self):
        columns = ["ID", "NAME", "MARKS"]
        data = [
            ["1", "Tommy", "85"],
            ["2", "Arthur", "75"],
            ["3", "John", "95"]
        ]
        avg = named_tuple(3, columns, data)
        self.assertEqual(avg, 85.0)
    def test2(self):
        columns = ["ID", "NAME", "MARKS"]
        data = [
            ["1", "Eleven", "90"],
            ["2", "Mike", "80"],
            ["3", "Dustin", "70"],
            ["4", "Lucas", "60"]
        ]
        avg = named_tuple(4, columns, data)
        self.assertEqual(avg, 75.0)
    def test3(self):
        columns = ["ID", "NAME", "MARKS"]
        data = [
            ["1", "Walter", "100"],
            ["2", "Jesse", "95"]
        ]
        avg = named_tuple(2, columns, data)
        self.assertEqual(avg, 97.5)
if __name__ == "__main__":
    unittest.main()