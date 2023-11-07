#####################################
#                                   #
#  Zestaw 5             07.11.2023  #
#                                   #
#           Zadanie 5.2             #
#            Plik main              #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

import fracs as Fr
import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(Fr.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(Fr.add_frac([7, -4], [1, 13]), [-87, 52])

    def test_sub_frac(self): 
        self.assertEqual(Fr.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(Fr.sub_frac([11, 121], [0, -3]), [1, 11])

    def test_mul_frac(self):
        self.assertEqual(Fr.mul_frac([-5, 2], [1, -10]), [1, 4])
        self.assertEqual(Fr.mul_frac([42, 50], [10, 7]), [6, 5])

    def test_div_frac(self):
        self.assertEqual(Fr.div_frac([1, 2], [1, 7]), [7, 2])
        self.assertEqual(Fr.div_frac([5, 2], [3, -4]), [-10, 3])

    def test_is_positive(self):
        self.assertEqual(Fr.is_positive([-1, 2]), False)
        self.assertEqual(Fr.is_positive([0, -5]), True)
        self.assertEqual(Fr.is_positive([1, -3]), False)
        self.assertEqual(Fr.is_positive([7, 4]), True)

    def test_is_zero(self):
        self.assertEqual(Fr.is_zero([1, 8]), False)
        self.assertEqual(Fr.is_zero([0, 1]), True)
        self.assertEqual(Fr.is_zero([0, -3]), True)

    def test_cmp_frac(self):
        self.assertEqual(Fr.cmp_frac([1, 3], [2, 6]), 0)
        self.assertEqual(Fr.cmp_frac([1, -4], [-2, 8]), 0)
        self.assertEqual(Fr.cmp_frac([1, 3], [1, 4]), 1)
        self.assertEqual(Fr.cmp_frac([-5, 11], [1, 3]), -1)

    def test_frac2float(self):
        self.assertEqual(Fr.frac2float([1, 4]), 0.25)
        self.assertEqual(Fr.frac2float([-2, 5]), -0.4)
        self.assertEqual(Fr.frac2float([0, -4]), 0)
        self.assertEqual(Fr.frac2float([1, 10000]), 0.0001)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
