#####################################
#                                   #
#  Zestaw 11            02.01.2024  #
#                                   #
#          Zadanie 11.2             #
#     Plik z klasa SingleList       #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self == other
            
class SingleList: