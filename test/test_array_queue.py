#!/usr/bin/python3

import unittest
from queue.array_queue import ArrayQueue


class TestArrayQueue(unittest.TestCase):
    def setUp(self):
        self.queue = ArrayQueue() 

    def test_init(self):
        self.assertEqual(self.queue.is_empty() > 0, True)

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.first(), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_first(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.first(), 1)


if __name__ == '__main__':
    unittest.main()
