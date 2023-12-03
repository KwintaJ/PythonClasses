#####################################
#                                   #
#  Zestaw 8             05.12.2023  #
#                                   #
#           Zadanie 8.2             #
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

    def testCenter(self):
        self.assertEqual(self.A.center(), Point(1.3333333333333333, 2))

    def testFromPoints(self):
        PointList = [Point(0, 0), Point(5, 2), Point(-1, 4)]
        B = Triangle.from_points(PointList)
        self.assertEqual(self.A, B)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
