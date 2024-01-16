#####################################
#                                   #
#  Zestaw 12            16.01.2024  #
#                                   #
#           Zadanie 12.8            #
#       Plik z implementacja        #
#          kolejki losowej          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

import random

class RandomQueue:
    def __init__(self, size=None): 
        self.sizeLimit = size
        self.queue = []
        
    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full")
        self.queue.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        index = random.randint(0, len(self.queue) - 1)
        self.queue[index], self.queue[-1] = self.queue[-1], self.queue[index]
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return self.sizeLimit is not None and len(self.queue) == self.sizeLimit

    def clear(self):
        self.queue = []