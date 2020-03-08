#!/usr/bin/python3

import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0 # count of actual elements
        self.capacity = 1 # default arracy capacity
        self.dynamic_array = self._make_dynamic_array(self._capacity) # init array

    def _make_dynamic_array(self, capcaity):
        return (capacity * ctypes.py_object)()
