#####################################
#                                   #
#  Zestaw 11            02.01.2024  #
#                                   #
#           Zadanie 11.2            #
#       Plik z implementacja        #
#         klasy SingleList          #
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
    def __init__(self):
        self.length = 0 
        self.head = None
        self.tail = None
        
    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current))
            current = current.next
        return "->".join(elements)

    def is_empty(self):
        return self.head is None

    def count(self): 
        return self.length

    def insert_head(self, node):
        if self.head: 
            node.next = self.head
            self.head = node
        else: 
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  
        if self.head: 
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("list is empty")
        node = self.head
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node 

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_max(self):
        if self.is_empty():
            return None
        current = self.head
        max_node = current
        while current:
            if current.data > max_node.data:
                max_node = current
            current = current.next
        return max_node

    def find_min(self):
        if self.is_empty():
            return None
        current = self.head
        min_node = current
        while current:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        return min_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head
    
