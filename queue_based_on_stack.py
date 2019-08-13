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
        self.active_stack = Stack()
        self.passive_stack = Stack()

    def size(self):
        return self.active_stack.size()

    def enqueue(self, item):
        self.active_stack.push(item)

    def dequeue(self):
        if self.active_stack.size() == 0:
            return None

        # Replacing all data to other stack (excepting last required element)
        for i in range(self.active_stack.size()-1):
            self.passive_stack.push(self.active_stack.pop())

        # Switching pointers
        tmp = self.active_stack
        self.active_stack = self.passive_stack
        self.passive_stack = tmp

        # Receiving required element
        return self.passive_stack.pop()
