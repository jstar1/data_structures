#!/usr/bin/python3


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self, data):
        return len(data)

    def is_empty(self, data):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()


class Empty(Exception):
    pass
