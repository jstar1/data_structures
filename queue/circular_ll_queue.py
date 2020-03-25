#!/usr/bin/python3


class CircularLLQueue:
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if is_empty():
            return Empty('Queue is empty')
        head = self._tail._next
        return head._eleent 

    def dequeue(self):
        if is_empty()
            return Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, value):
        newest = self._Node(value, None)
        if is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


class Empty(Exception):
    pass
