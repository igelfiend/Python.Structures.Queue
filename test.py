#!/usr/bin/env python
# coding=utf8

import unittest
from main import Queue


class QueueTesting(unittest.TestCase):
    # ---------- TEST ENQUEUE ----------------------
    def test_enqueue_single_element_in_empty_queue(self):
        queue = Queue()
        queue.enqueue(1)

        test_result = queue.queue
        check_result = [1]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue single element in empty queue. Result array are not equal.")

    def test_enqueue_multiple_elements_in_empty_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        test_result = queue.queue
        check_result = [1, 2, 3]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue multiple elements in empty queue. Result array are not equal.")

    def test_enqueue_single_element_in_ready_queue(self):
        queue = Queue()
        queue.queue = [1, 2]
        queue.enqueue(3)

        test_result = queue.queue
        check_result = [1, 2, 3]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue single element in ready queue. Result array are not equal.")

    def test_enqueue_multiple_elements_in_ready_queue(self):
        queue = Queue()
        queue.queue = [1, 2]
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        test_result = queue.queue
        check_result = [1, 2, 3, 4, 5]

        self.assertEqual(test_result, check_result,
                         "Testing 'Enqueue'. Enqueue multiple elements in ready queue. Result array are not equal.")

    # ------------- TEST DEQUEUE ---------------------------------

    def test_dequeue_from_normal_queue(self):
        queue = Queue()
        queue.queue = [1, 2, 3, 4, 5]

        test_value = queue.dequeue()
        check_value = 1

        test_result = queue.queue
        check_result = [2, 3, 4, 5]

        self.assertEqual(test_result, check_result,
                         "Testing 'Dequeue'. Dequeue from normal queue. Result array are not equal.")

        self.assertEqual(test_value, check_value,
                         "Testing 'Dequeue'. Dequeue from normal queue. Dequeued value incorrect.")

    def test_dequeue_from_empty_queue(self):
        queue = Queue()
        queue.queue = []

        test_value = queue.dequeue()

        test_result = queue.queue
        check_result = []

        self.assertEqual(test_result, check_result,
                         "Testing 'Dequeue'. Dequeue from empty queue. Result array are not equal.")

        self.assertIsNone(test_value,
                         "Testing 'Dequeue'. Dequeue from normal queue. Dequeued value incorrect.")



if __name__ == '__main__':
    unittest.main()
