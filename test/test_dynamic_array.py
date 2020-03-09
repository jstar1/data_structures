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
        self.assertTrue('invalid index' in str(context.exception))

    def  test_append(self):
        self.array.append(1)
        self.assertEqual(self.array[0] == 1, True)


if __name__ == '__main__':
    unittest.main()    
