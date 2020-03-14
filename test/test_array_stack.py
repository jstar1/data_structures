#!/usr/bin/python3

import unittest
from stack.array_stack import ArrayStack


class TestArrayStack(unittest.TestCase):
    def setUp(self):
        self.stack = ArrayStack()

    def test_failure(self):
        with self.assertRaises(Exception) as context:
            self.stack.pop()
        self.assertTrue("Stack is empty" in str(context.exception))

    def test_len(self):
        self.assertEqual(len(self.stack) == 0, True)

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(len(self.stack) == 1, True)

    def test_top(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top() == 1, True)

    def test_push_multi(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.top() == 3, True)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop() == 2, True)
        self.assertEqual(self.stack.top() == 1, True)
        self.assertEqual(self.stack.pop() == 1, True)
        self.assertEqual(len(self.stack) == 0, True)
        self.assertTrue(self.stack.is_empty())

    def test_repr(self):
        self.stack.push(1)
        self.assertEqual(eval(repr(self.stack)) == [1], True)
        self.stack.push(2)
        self.assertEqual(eval(repr(self.stack)) == [1, 2], True)
        self.stack.push(3)
        self.assertEqual(eval(repr(self.stack)) == [1, 2, 3], True)
        self.stack.push(4)
        self.assertEqual(eval(repr(self.stack)) == [1, 2, 3, 4], True)
        

if __name__ == '__main__':
    unittest.main()
