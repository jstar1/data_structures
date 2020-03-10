#!/usr/bin/python3

import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0  # count of actual elements
        self._capacity = 1  # default arracy capacity
        self._dynamic_array = self._make_dynamic_array(self._capacity)  # init array

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._dynamic_array[k]

    def __repr__(self):
        return str(self._dynamic_array[: self._n])

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._dynamic_array[self._n] = obj
        self._n += 1

    def extend(self, iterable=[]):
        for ele in iterable:
            self.append(ele)
    
    def insert(self, index, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, index, - 1):
            self._dynamic_array[j] = self._dynamic_array[j-1]
        self._dynamic_array[index] = obj
        self._n += 1
        
    def _resize(self, new_capacity):
        bigger_array = self._make_dynamic_array(new_capacity)
        for i in range(self._n):
            bigger_array[i] = self._dynamic_array[i]
        self._dynamic_array = bigger_array
        self._capacity = new_capacity

    def pop(self, pos=None):
        if len(self._dynamic_array) == 0:
            raise IndexError("pop from empty list")
        del_val = None
        if pos is None or pos == self._n - 1:
            del_val = self._dynamic_array[self._n - 1]
            self._dynamic_array[self._n - 1] is None
            self._n -= 1
            return del_val
        if 0 <= pos < self._n:
            for j in range(pos, self._n - 1):
                if j == pos:
                    del_val = self._dynamic_array[j]
                self._dynamic_array[j] = self._dynamic_array[j + 1]
            self._dynamic_array[self._n - 1] = None
            self._n -= 1
            return del_val
        raise IndexError("invalid index")

    def remove(self, value):
        for i in range(self._n):
            if self._dynamic_array[i] == value:
                for j in range(i, self._n - 1):
                    self._dynamic_array[j] = self._dynamic_array[j + 1]
                self._dynamic_array[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("value not found")

    def _make_dynamic_array(self, capacity):
        return (capacity * ctypes.py_object)()

