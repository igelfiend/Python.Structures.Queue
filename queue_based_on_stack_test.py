#!/usr/bin/env python
# coding=utf8

import unittest
from queue_based_on_stack import StackBasedQueue


class StackBasedQueueTesting(unittest.TestCase):
    # ---------- TEST ENQUEUE ----------------------
    def test_enqueue_single_element_in_empty_queue(self):
        queue = StackBasedQueue()
        queue.enqueue(1)

        test_result = queue.stack.stack
        check_result = [1]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue single element in empty queue. Result array are not equal.")

    def test_enqueue_multiple_elements_in_empty_queue(self):
        queue = StackBasedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        test_result = queue.stack.stack
        check_result = [3, 2, 1]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue multiple elements in empty queue. Result array are not equal.")

    def test_enqueue_single_element_in_ready_queue(self):
        queue = StackBasedQueue()
        queue.stack.stack = [2, 1]
        queue.enqueue(3)

        test_result = queue.stack.stack
        check_result = [3, 2, 1]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue single element in ready queue. Result array are not equal.")

    def test_enqueue_multiple_elements_in_ready_queue(self):
        queue = StackBasedQueue()
        queue.stack.stack = [2, 1]
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        test_result = queue.stack.stack
        check_result = [5, 4, 3, 2, 1]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue multiple elements in ready queue. Result array are not equal.")

    # ------------- TEST DEQUEUE ---------------------------------

    def test_dequeue_from_normal_queue(self):
        queue = StackBasedQueue()
        queue.stack.stack = [5, 4, 3, 2, 1]

        test_value = queue.dequeue()
        check_value = 1

        test_result = queue.stack.stack
        check_result = [5, 4, 3, 2]

        self.assertEqual(test_result, check_result,
                         "Testing 'Dequeue'. Dequeue from normal queue. Result array are not equal.")

        self.assertEqual(test_value, check_value,
                         "Testing 'Dequeue'. Dequeue from normal queue. Dequeued value incorrect.")

    def test_dequeue_from_empty_queue(self):
        queue = StackBasedQueue()
        queue.queue = []

        test_value = queue.dequeue()

        test_result = queue.stack.stack
        check_result = []

        self.assertEqual(test_result, check_result,
                         "Testing 'Dequeue'. Dequeue from empty queue. Result array are not equal.")

        self.assertIsNone(test_value,
                         "Testing 'Dequeue'. Dequeue from normal queue. Dequeued value incorrect.")

    def test_dequeue_full_queue(self):
        queue = StackBasedQueue()
        queue.stack.stack = [5, 4, 3, 2, 1]

        test_result = []
        for i in range(5):
            test_result.append(queue.dequeue())

        check_result = [1, 2, 3, 4, 5]

        self.assertEqual(queue.stack.stack, [],
                         "Testing 'Dequeue'. Dequeue from normal queue. Result array are not equal.")

        self.assertEqual(test_result, check_result,
                         "Testing 'Dequeue'. Dequeue from normal queue. Dequeued list incorrect.")


if __name__ == '__main__':
    unittest.main()
