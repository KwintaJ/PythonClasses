#####################################
#                                   #
#  Zestaw 7             28.11.2023  #
#                                   #
#           Zadanie 7.3             #
#     Plik z modulem rectangles     #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):  # konstuktor
        if not x1 < x2 or not y1 < y2:
            raise ValueError("wrong values")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == self.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point(round((self.pt1.x + self.pt2.x) / 2, 8), round((self.pt1.y + self.pt2.y) / 2, 8))
        
    def area(self):
        return round((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y), 8)

    def move(self, x, y):
        M = Point(x, y)
        return Rectangle((self.pt1 + M).x, (self.pt1 + M).y, (self.pt2 + M).x, (self.pt2 + M).y)

    def intersection(self, other):
        if self.pt2.x <= other.pt1.x or self.pt2.y <= other.pt1.y or self.pt1.x >= other.pt2.x or self.pt1.y >= other.pt2.y:
            raise ValueError("overlap is not a rectangle")
        Ax = max(self.pt1.x, other.pt1.x)
        Ay = max(self.pt1.y, other.pt1.y)
        Bx = min(self.pt2.x, other.pt2.x)
        By = min(self.pt2.y, other.pt2.y)
        return Rectangle(Ax, Ay, Bx, By)

    def cover(self, other):
        Ax = min(self.pt1.x, other.pt1.x)
        Ay = min(self.pt1.y, other.pt1.y)
        Bx = max(self.pt2.x, other.pt2.x)
        By = max(self.pt2.y, other.pt2.y)
        return Rectangle(Ax, Ay, Bx, By)

    def make4(self):
        A = self.pt1
        C = self.pt2
        S = self.center()
        K = Point((A.x + C.x) / 2, A.y)
        L = Point(C.x, (A.y + C.y) / 2)
        M = Point((A.x + C.x) / 2, C.y)
        N = Point(A.x, (A.y + C.y) / 2)
        Rect1 = Rectangle(A.x, A.y, S.x, S.y)
        Rect2 = Rectangle(K.x, K.y, L.x, L.y)
        Rect3 = Rectangle(S.x, S.y, C.x, C.y)
        Rect4 = Rectangle(N.x, N.y, M.x, M.y)
        return [Rect1, Rect2, Rect3, Rect4]
        
