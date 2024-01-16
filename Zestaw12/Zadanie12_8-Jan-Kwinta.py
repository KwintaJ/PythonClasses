import unittest
from randomQueueModule import RandomQueue

class TestRandomQueue(unittest.TestCase):
    def test_insert_and_remove(self):
        q = RandomQueue()
        q.insert(1)
        self.assertFalse(q.is_empty())
        item = q.remove()
        self.assertEqual(item, 1)
        self.assertTrue(q.is_empty())

    def test_insert_full_queue(self):
        q = RandomQueue(size=2)
        q.insert(1)
        q.insert(2)
        with self.assertRaises(ValueError):
            q.insert(3)

    def test_remove_empty_queue(self):
        q = RandomQueue()
        with self.assertRaises(ValueError):
            q.remove()

    def test_clear(self):
        q = RandomQueue()
        q.insert(1)
        q.insert(2)
        q.clear()
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()