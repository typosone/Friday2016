import unittest

import t1001


class Test1001(unittest.TestCase):
    def test_true_check_sum_2times_over_60(self):
        self.assertTrue(t1001.check_sum_2times_over_60(15, 16))
        self.assertTrue(t1001.check_sum_2times_over_60(1, 30))
        self.assertTrue(t1001.check_sum_2times_over_60(2, 29))
        self.assertTrue(t1001.check_sum_2times_over_60(3, 28))
        self.assertTrue(t1001.check_sum_2times_over_60(4, 27))
        self.assertTrue(t1001.check_sum_2times_over_60(5, 26))
        self.assertTrue(t1001.check_sum_2times_over_60(6, 25))
        self.assertTrue(t1001.check_sum_2times_over_60(7, 24))
        self.assertTrue(t1001.check_sum_2times_over_60(8, 23))
        self.assertTrue(t1001.check_sum_2times_over_60(9, 22))
        self.assertTrue(t1001.check_sum_2times_over_60(10, 21))
        self.assertTrue(t1001.check_sum_2times_over_60(11, 20))
        self.assertTrue(t1001.check_sum_2times_over_60(12, 19))
        self.assertTrue(t1001.check_sum_2times_over_60(13, 18))
        self.assertTrue(t1001.check_sum_2times_over_60(14, 17))
        self.assertTrue(t1001.check_sum_2times_over_60(15, 16))
        self.assertTrue(t1001.check_sum_2times_over_60(16, 15))

    def test_false_check_sum_2times_over_60(self):
        self.assertFalse(t1001.check_sum_2times_over_60(1, 29))
        self.assertFalse(t1001.check_sum_2times_over_60(2, 28))
        self.assertFalse(t1001.check_sum_2times_over_60(3, 27))
        self.assertFalse(t1001.check_sum_2times_over_60(4, 26))
        self.assertFalse(t1001.check_sum_2times_over_60(5, 25))
        self.assertFalse(t1001.check_sum_2times_over_60(6, 24))
        self.assertFalse(t1001.check_sum_2times_over_60(7, 23))
        self.assertFalse(t1001.check_sum_2times_over_60(8, 22))
        self.assertFalse(t1001.check_sum_2times_over_60(9, 21))
        self.assertFalse(t1001.check_sum_2times_over_60(10, 20))
        self.assertFalse(t1001.check_sum_2times_over_60(11, 19))
        self.assertFalse(t1001.check_sum_2times_over_60(12, 18))
        self.assertFalse(t1001.check_sum_2times_over_60(13, 17))
        self.assertFalse(t1001.check_sum_2times_over_60(14, 16))
        self.assertFalse(t1001.check_sum_2times_over_60(15, 15))
        self.assertFalse(t1001.check_sum_2times_over_60(16, 14))

    def test_true_tax_include(self):
        for cost in range(4630, 1000, 5):
            self.assertTrue(t1001.tax_include(cost))

    def test_false_tax_include(self):
        for cost in range(1, 4630):
            self.assertFalse(t1001.tax_include(cost))

    def test_rank_f_judge_rank(self):
        for score in range(-100, 45):
            self.assertEqual(t1001.judge_rank(score), 'F')

    def test_rank_c_judge_rank(self):
        for score in range(45, 60):
            self.assertEqual(t1001.judge_rank(score), 'C')

    def test_rank_b_judge_rank(self):
        for score in range(60, 80):
            self.assertEqual(t1001.judge_rank(score), 'B')

    def test_rank_a_judge_rank(self):
        for score in range(80, 200):
            self.assertEqual(t1001.judge_rank(score), 'A')

    def test_factorial(self):
        self.assertEqual(t1001.factorial(0), 1)
        self.assertEqual(t1001.factorial(1), 1)
        self.assertEqual(t1001.factorial(2), 2)
        self.assertEqual(t1001.factorial(3), 6)
        self.assertEqual(t1001.factorial(4), 24)
        self.assertEqual(t1001.factorial(5), 120)
        self.assertEqual(t1001.factorial(6), 720)
        self.assertEqual(t1001.factorial(7), 5040)
        self.assertEqual(t1001.factorial(8), 40320)
        self.assertEqual(t1001.factorial(9), 362880)
        self.assertEqual(t1001.factorial(10), 3628800)

    def test_power_of_two(self):
        for num in range(0, 10):
            self.assertEqual(t1001.power_of_two(num), 2 ** num)


if __name__ == '__main__':
    unittest.main()