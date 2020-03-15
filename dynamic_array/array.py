#!/usr/bin/python3

import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0 # Number of elements inside array
        self._capacity = 1 # Actual length of array
        self.array = None
    
    def __repr__(self):
        return str(self.array[:self._n])

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        pass

    def _ressize(self, cap):
       pass
 
    def _create(self, cap):
        pass

    def append(self, obj):
        pass

    def insert(self, obj):
        pass
   
    def extend(self, iterable=[]):
        pass 

    def remove(self, obj):
        pass

    def pop(self, pos=None):
        pass

