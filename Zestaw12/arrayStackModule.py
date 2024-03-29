#####################################
#                                   #
#  Zestaw 12            16.01.2024  #
#                                   #
#           Zadanie 12.2            #
#       Plik z implementacja        #
#          tablicowa stosu          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

class Stack:
    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data