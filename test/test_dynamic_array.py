#!/usr/bin/python3

import unittest
from dynamic_array.array import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()

    def test_len(self):
        self.assertEqual(len(self.array) == 0, True)

    def test_getitem(self):
        with self.assertRaises(IndexError) as context:
            self.array[10]
        self.assertTrue("invalid index" in str(context.exception))

    def test_append(self):
        self.array.append(1)
        self.assertEqual(self.array[0] == 1, True)

    def test_extend(self):
        self.array.extend([1, 2, 3])
        self.assertEqual(len(self.array) == 3, True)

    def test_pop(self):
        self.array.append(1)
        self.assertEqual(self.array.pop() == 1, True)

    def test_pop_failure(self):
        with self.assertRaises(IndexError) as context:
            self.array.pop(20)
        self.assertTrue("invalid index" in str(context.exception))

    def test_pop_remove_index(self):
        self.array.extend([1, 2, 3, 4, 5])
        self.assertEqual(self.array.pop(3) == 4, True)

    def test_remove(self):
        self.array.extend([1, 2, 3, 4, 5])
        self.array.remove(3)
        self.assertEqual(eval(repr(self.array)), [1, 2, 4, 5])

    def test_repr(self):
        self.array.extend([1, 2, 3, 4, 5])
        self.assertEqual(eval(repr(self.array)) == [1, 2, 3, 4, 5], True)

    def test_insert(self):
        self.array.extend([1, 2, 4, 5])
        self.array.insert(2, 3) 
        self.assertEqual(eval(repr(self.array)) == [1, 2, 3, 4, 5], True)


if __name__ == "__main__":

    unittest.main()
