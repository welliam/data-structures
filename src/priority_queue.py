# -*- coding: utf-8 -*-

"""Implement the Priority Queue abstract data type."""

from .binary_heap import BinaryHeap


class _Prioritized(object):
    def __init__(self, value, priority, order):
        self.value = value
        self.priority = priority
        self.order = order

    def __lt__(self, p):
        if self.priority == p.priority:
            return self.order < p.order
        return self.priority < p.priority

    def __repr__(self):
        return "Priortizied" + str((self.value, self.priority, self.order))


class PriorityQueue(object):
    """Implement a priority queue."""

    def __init__(self, iterable=None):
        """Initialize a new priority queue.

        If iterable is provided, """
        self._heap = BinaryHeap(iterable=None)
        self._order = 0
        if iterable:
            for item, priority in iterable:
                self.insert(item, priority)

    def insert(self, item, priority):
        """Insert item into priority queue with a given priority.

        Priority is expected to be value that can be compared with
        less than. A "lower" value indicates a higher priority."""
        self._heap.push(_Prioritized(item, priority, self._order))
        self._order += 1

    def pop(self):
        """Pops off the highest priority value."""
        return self._heap.pop().value

    def peek(self):
        """Peeks at the highest priority value without removing it."""
        return self._heap.peek().value
