#####################################
#                                   #
#  Zestaw 11            02.01.2024  #
#                                   #
#           Zadanie 11.2            #
#          Plik testujacy           #
#         klase SingleList          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8
from SingleLists import SingleList, Node
import unittest

class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.my_list = SingleList()
        self.node1 = Node(22)
        self.my_list.insert_head(self.node1)
        self.my_list.insert_head(Node(1))
        self.my_list.insert_head(Node(3))
        self.my_list.insert_head(Node(6))
        self.my_list.insert_tail(Node(-2))
        self.my_list.insert_tail(Node(109))
        self.my_list.insert_tail(Node(-10))
        

    def test_inserts(self):
        self.assertEqual(str(self.my_list), "6->3->1->22->-2->109->-10")

    def test_search(self):
        searched_node1 = self.my_list.search(22)
        self.assertEqual(searched_node1, self.node1)
        searched_node2 = self.my_list.search(100)
        self.assertEqual(searched_node2, None)

    def test_find_max(self):
        max_node = self.my_list.find_max()
        self.assertEqual(max_node.data, 109)

    def test_find_min(self):
        min_node = self.my_list.find_min()
        self.assertEqual(min_node.data, -10)

    def test_reverse(self):
        self.my_list.reverse()
        self.assertEqual(str(self.my_list), "-10->109->-2->22->1->3->6")

if __name__ == '__main__':
    unittest.main()
