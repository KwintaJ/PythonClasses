######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#       Plik z klasa ConvexHull      #
#          Algorytm Grahama          #
#                                    #
######################################

from math import atan2
from points import Point
from vectors import Vector

class ConvexHull:
    def __init__(self, L):
        self.pointsList = L
        self.hullList = self.computeHull()
        
    def computeHull(self):
        if len(self.pointsList) < 3:
            return self.pointsList  
        
        pivot = min(self.pointsList, key=lambda p: (p.y, p.x))
        sorted_points = sorted(self.pointsList, 
                               key=lambda p: (atan2(p.y - pivot.y, 
                                              p.x - pivot.x), p))

        hull = [pivot, sorted_points[0], sorted_points[1]]

        for point in sorted_points[2:]:
            while len(hull) > 1 and \
            (Vector(hull[-2], hull[-1]).cross(Vector(hull[-2], point)) <= 0):
                hull.pop()
            hull.append(point)
            
        if hull[0] == hull[1]:
            hull.pop(0)

        return hull
    
    def getHull(self):
        return self.hullList

