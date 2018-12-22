import unittest
from small import double_nine, duplicated_list


class TestTrans(unittest.TestCase):
    def test_double_nine_left(self):
        result = "1\n2  4\n3  6  9\n4  8 12 16\n5 10 15 20 25\n6 12 18 24 30 36\n7 14 21 28 35 42 49\n8 16 24 32 40 48 56 64\n9 18 27 36 45 54 63 72 81\n"
        self.assertEqual(double_nine(), result)

    def test_duplicated_list(self):
        self.assertEqual(
            duplicated_list([1, 2, 3, 2, 1, 10, 5, 5, 1]), [1, 2, 2, 1, 5, 5, 1]
        )


if __name__ == "__main__":
    unittest.main()
