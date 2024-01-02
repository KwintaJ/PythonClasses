#####################################
#                                   #
#  Zestaw 6             21.11.2023  #
#                                   #
#           Zadanie 6.2             #
#       Plik z modulem points       #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

from math import sqrt as Msqrt

class Point:

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return Msqrt(self.x ** 2 + self.y ** 2)
    
    def __hash__(self):
        return hash((self.x, self.y))

