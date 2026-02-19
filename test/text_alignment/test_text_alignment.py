import unittest
from src.text_alignment.util import align_text


class test_text_align(unittest.TestCase):

    def test_thickness_2(self):
        res = align_text(2, "A")
        first = res[0].strip()
        self.assertEqual(first, "A")
        belt = False
        for ln in res:
            if ln.strip() == "A" * (2 * 6):
                belt = True
        self.assertTrue(belt)
        last = res[-1].strip()
        self.assertEqual(last, "A")

    def test_thickness_3(self):
        res = align_text(3, "B")

        first = res[0].strip()
        self.assertEqual(first, "B")

        belt = False
        for ln in res:
            if ln.strip() == "B" * (3 * 6):
                belt = True
        self.assertTrue(belt)

        last = res[-1].strip()
        self.assertEqual(last, "B")

    def test_thickness_5(self):
        res = align_text(5, "H")

        belt = False
        for ln in res:
            if ln.strip() == "H" * 30:
                belt = True
        self.assertTrue(belt)

        last = res[-1].strip()
        self.assertEqual(last, "H")

    def test_char_used(self):
        res = align_text(4, "X")

        for ln in res:
            for ch in ln:
                if ch != "X" and ch != " ":
                    self.fail("Unexpected char")


if __name__ == "__main__":
    unittest.main()