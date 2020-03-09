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
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self.dynamic_array[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self.dynamic_array[self._n] = obj
        self._n += 1
    
    def _resize(self, new_capacity):
        bigger_array = self._make_dynamic_array(new_capacity)
        for i in range(self._n):
            bigger_array[i] = self.dynamic_array[i]
        self.dynamic_array = bigger_array
        self._capacity = new_capcaity    

    def _make_dynamic_array(self, capacity):
        return (capacity * ctypes.py_object)()
