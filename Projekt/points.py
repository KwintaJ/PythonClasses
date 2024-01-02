######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#        Plik z modulem Point        #
#                                    #
######################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other