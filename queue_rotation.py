#!/usr/bin/env python
# coding=utf8

from copy import deepcopy
from random import randint


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


def queue_rotation(queue_size, iterations_count):
    # Creating and initializing queue
    queue = Queue()
    for i in range(queue_size):
        queue.enqueue(randint(0, 42))

    for i in range(iterations_count):
        queue.enqueue(queue.dequeue())
        print("Queue status: {0}".format(queue.queue))
