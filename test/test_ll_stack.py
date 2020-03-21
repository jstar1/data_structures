#!/usr/bin/python3

import unittest
from stack.ll_stack import LinkedStack

class TestLinkedStack(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedStack()
    
    def test_init(self):
        self.assertIsNotNone(self.stack)    

    def test_len(self):
        self.assertEqual(len(self.stack), 0)

    def test_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(len(self.stack), 1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(repr(self.stack),'3 -> ') 

    def test_top(self):
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertTrue(self.stack.top(), 5)
        self.assertEqual(repr(self.stack), '5 -> 4 -> 3 -> ')

    def test_pop(self):
        self.stack.push(3)
        self.stack.push(6)
        self.stack.push(7)
        self.assertEqual(self.stack.top(), 7)

    def test_exception(self):
        with self.assertRaises(Exception) as context:
            self.stack.pop()
        self.assertTrue("Stack is empty" in str(context.exception))

        with self.assertRaises(Exception) as context:
            self.stack.top()
        self.assertTrue("Stack is empty" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
