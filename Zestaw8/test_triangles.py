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
        self.assertEqual(self.A.center, Point(1.3333333333333333, 2))

    def testFromPoints(self):
        PointList = [Point(0, 0), Point(5, 2), Point(-1, 4)]
        B = Triangle.from_points(PointList)
        self.assertEqual(self.A, B)

    def testTop(self):
        self.assertEqual(self.A.top, 4)

    def testLeft(self):
        self.assertEqual(self.A.left, -1)

    def testBottom(self):
        self.assertEqual(self.A.bottom, 0)

    def testRight(self):
        self.assertEqual(self.A.right, 5)

    def testWidth(self):
        self.assertEqual(self.A.width, 6)

    def testHeight(self):
        self.assertEqual(self.A.height, 4)

    def testTopLeft(self):
        self.assertEqual(self.A.topleft, Point(-1, 4))

    def testBottomLeft(self):
        self.assertEqual(self.A.bottomleft, Point(-1, 0))

    def testTopRight(self):
        self.assertEqual(self.A.topright, Point(5, 4))

    def testBottomRight(self):
        self.assertEqual(self.A.bottomright, Point(5, 0))

    def testArea(self):
        self.assertEqual(self.A.area(), 10.0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()