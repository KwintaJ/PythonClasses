######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#       Plik z modulem Vector        #
#                                    #
######################################

from points import Point

class Vector:
    def __init__(self, A, B):
        self.pointA = A
        self.pointB = B

    def __str__(self):
        return "[" + str(self.pointA) + ", " + str(self.pointB) + "]"

    def __eq__(self, other):
        return self.pointA == other.pointA and self.pointB == other.pointB

    def __ne__(self, other):
        return not self == other
        
    def cross(self, other):
        return (self.pointB.x - self.pointA.x) * 
               (other.pointB.y - other.pointA.y) - 
               (self.pointB.y - self.pointA.y) * 
               (other.pointB.x - other.pointA.x)
