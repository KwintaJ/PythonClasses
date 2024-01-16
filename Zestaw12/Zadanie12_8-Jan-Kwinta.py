#####################################
#                                   #
#  Zestaw 12            16.01.2024  #
#                                   #
#           Zadanie 12.8            #
#   Plik z testujacy implementacje  #
#          kolejki losowej          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

import unittest
from randomQueueModule import RandomQueue

class TestRandomQueue(unittest.TestCase):
    def testInsertAndERmove(self):
        q = RandomQueue()
        q.insert(1)
        self.assertFalse(q.is_empty())
        item = q.remove()
        self.assertEqual(item, 1)
        self.assertTrue(q.is_empty())

    def testInsertIntoFullQueue(self):
        q = RandomQueue(size=2)
        q.insert(1)
        q.insert(2)
        with self.assertRaises(ValueError):
            q.insert(3)

    def testRemoveEmptyQueue(self):
        q = RandomQueue()
        with self.assertRaises(ValueError):
            q.remove()

    def testClear(self):
        q = RandomQueue()
        q.insert(1)
        q.insert(2)
        q.clear()
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()