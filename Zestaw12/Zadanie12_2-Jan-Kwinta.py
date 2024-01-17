#####################################
#                                   #
#  Zestaw 12            16.01.2024  #
#                                   #
#           Zadanie 12.2            #
#   Plik testujacy implementacje    #
#          tablicowa stosu          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

# !/usr/bin/env/python
# coding = utf-8
import unittest
from arrayStackModule import Stack

class TestStack(unittest.TestCase):
    def testPushPop(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def testEmptyStackPop(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def testFullStackPush(self):
        s = Stack(2)
        s.push(1)
        s.push(2)
        with self.assertRaises(OverflowError):
            s.push(3)

    def testIsEmpty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

    def testIsFull(self):
        s = Stack(2)
        self.assertFalse(s.is_full())
        s.push(1)
        s.push(2)
        self.assertTrue(s.is_full())

if __name__ == '__main__':
    unittest.main()
