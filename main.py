#!/usr/bin/env python
# coding=utf8

from copy import deepcopy


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            value = deepcopy(self.queue[0])
            del self.queue[0]
            return value

    def size(self):
        return len(self.queue)
