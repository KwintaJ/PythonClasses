######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#       Plik z klasa ConvexHull      #
#                                    #
######################################

from points import Point
from vectors import Vector

class ConvexHull:
    def __init__(self, L):
        self.pointsList = L
        self.hullList = []
