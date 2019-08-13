#!/usr/bin/env python
# coding=utf8

from copy import deepcopy


class Stack:
    """
    Class represents stack container interface.
    Provides push, pop and peek functions.
    """
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.stack:
            return None
        else:
            value = deepcopy(self.stack[0])
            del self.stack[0]
            return value

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[0]


class StackBasedQueue:
    def __init__(self):
        self.stack = Stack()
        self.temp_stack = Stack()

    def size(self):
        return self.stack.size()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        if self.stack.size() == 0:
            return None

        # Replacing all data to temp stack (excepting last required element)
        for i in range(self.stack.size()-1):
            self.temp_stack.push(self.stack.pop())

        # Receiving data
        value = deepcopy(self.stack.pop())

        # Returning all data back
        for i in range(self.temp_stack.size()):
            self.stack.push(self.temp_stack.pop())

        # Receiving required element
        return value
