#!/usr/bin/python3

import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0 # count of actual elements
        self._capacity = 1 # default arracy capacity
        self.dynamic_array = self._make_dynamic_array(self._capacity) # init array

    def  __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if 0 <= k < self._n:
            raise IndexError('invalid index')
        return self.dynamic_array[k]

    def _make_dynamic_array(self, capacity):
        return (capacity * ctypes.py_object)()
