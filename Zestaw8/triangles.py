#####################################
#                                   #
#  Zestaw 6             21.11.2023  #
#                                   #
#           Zadanie 6.4             #
#     Plik z modulem triangles      #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

from points import Point
from math import sqrt as Msqrt

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):  # konstuktor
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def from_points(pointsList):
        Tr = Triangle(0, 0, 0, 0, 0, 0)
        Tr.pt1 = pointsList[0]
        Tr.pt2 = pointsList[1]
        Tr.pt3 = pointsList[2]
        return Tr

    def __str__(self):
        return "[" + str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) + "]"

    def __repr__(self):
        return "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")"

    def __eq__(self, other):
        if self.pt1 != other.pt1 and self.pt1 != other.pt2 and self.pt1 != other.pt3:
            return False
        if self.pt2 != other.pt1 and self.pt2 != other.pt2 and self.pt2 != other.pt3:
            return False
        if self.pt3 != other.pt1 and self.pt3 != other.pt2 and self.pt3 != other.pt3:
            return False
        return True
        

	def __ne__(self, other):
        return not self == other

	@property
    def center(self):
        S = self.pt1 + self.pt2 + self.pt3
        return Point(S.x / 3, S.y / 3)
        
    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def area(self):
        a = (self.pt2 - self.pt1).length()
        b = (self.pt3 - self.pt2).length()
        c = (self.pt1 - self.pt3).length()
        return (Msqrt((a + b + c) * (b + c - a) * (a - b + c) * (a + b - c))) / 4

    def move(self, x, y):
        M = Point(x, y)
        return Triangle(self.pt1 + M, self.pt2 + M, self.pt3 + M)

