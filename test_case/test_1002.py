import unittest

from training import t1002


class Test1002(unittest.TestCase):
    def test_hoge(self):
        self.assertTrue(t1002.hoge())

    def test_201607(self):
        expected = [
            [0, 0, 0, 0, 0, 1, 2],
            [3, 4, 5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29, 30],
            [31, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(t1002.cal(2016, 7), expected)

    def test_204611(self):
        expected = [
            [0, 0, 0, 0, 1, 2, 3],
            [4, 5, 6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, ],
        ]
        self.assertEqual(t1002.cal(2046, 11), expected)

    def test_188602(self):
        expected = [
            [0, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
            [14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27],
            [28, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(t1002.cal(1886, 2), expected)

    def test_190002(self):
        expected = [
            [0, 0, 0, 0, 1, 2, 3],
            [4, 5, 6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 0, 0, 0],
        ]
        self.assertEqual(t1002.cal(1900, 2), expected)

    def test_200002(self):
        expected = [
            [0, 0, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 0, 0, 0, 0],
        ]
        self.assertEqual(t1002.cal(2000, 2), expected)