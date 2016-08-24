# -*- coding: utf-8 -*-

"""Implement the Priority Queue abstract data type."""

from binary_heap import BinaryHeap
from collections import namedtuple


Prioritized = namedtuple('Prioritized', ['value', 'priority'])


class PriorityQueue(object):
    """Implement a priority queue."""
    def __init__(self, iterable=None):
        """Initialize a new priority queue.

        If iterable is provided, """
        self._heap = BinaryHeap(
            iterable=None,
            compare=lambda a, b: a.priority < b.priority
        )
        if iterable:
            for item, priority in iterable:
                self.insert(item, priority)

    def insert(self, item, priority):
        """Insert item into priority queue with a given priority.

        Priority is expected to be value that can be compared with
        less than. A "lower" value indicates a higher priority."""
        self._heap.push(Prioritized(item, priority))

    def pop(self):
        """Pops off the highest priority value."""
        return self._heap.pop().value

    def peek(self):
        """Peeks at the highest priority value without removing it."""
        return self._heap.peek().value
