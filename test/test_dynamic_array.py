#!/usr/bin/python3

import unittest
from dynamic_array.array import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()

    def test_len(self):
        self.assertEqual(len(self.array) == 0, True)

if __name__ == '__main__':
    unittest.main()    
