#####################################
#                                   #
#  Zestaw 6             21.11.2023  #
#                                   #
#           Zadanie 6.4             #
#          Plik testujacy           #
#          modul triangles          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

from points import Point
from triangles import Triangle
import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.A = Triangle(0, 0, 5, 2, -1, 4)
        self.B = Triangle(-2, -2.4, 0.3, 6.1, 5, -1)
        self.C = Triangle(5, 2, 0, 0, -1, 4)

    def testStr(self):
        self.assertEqual(str(self.A), "[(0, 0), (5, 2), (-1, 4)]")
        self.assertEqual(str(self.B), "[(-2, -2.4), (0.3, 6.1), (5, -1)]")

    def testRepr(self):
        self.assertEqual(repr(self.A), "Triangle(0, 0, 5, 2, -1, 4)")
        self.assertEqual(repr(self.B), "Triangle(-2, -2.4, 0.3, 6.1, 5, -1)")

    def testEqual(self):
        self.assertEqual(self.A == self.A, True)
        self.assertEqual(self.A == self.C, True)
        self.assertEqual(self.A == self.B, False)

    def testNotEqual(self):
        self.assertEqual(self.A != self.A, False)
        self.assertEqual(self.A != self.B, True)
    
    def testCenter(self):
        self.assertEqual(self.A.center(), Point(1.33333333, 2))
        self.assertEqual(self.B.center(), Point(1.1, 0.9))

    def testArea(self):
        self.assertEqual(self.A.area(), 11)
        self.assertEqual(self.B.area(), 28.14)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
