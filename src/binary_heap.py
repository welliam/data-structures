# -*- coding: utf-8 -*-

"""Implement binary heap abstract data type."""


def _children(i):
    """Define math to find children of the parent."""
    return 2 * i + 1, 2 * i + 2


def _parent(i):
    """Define math to find parent of a child."""
    return (i - 1) // 2


class BinaryHeap(object):
    """Implement a binary heap.

    Optionally takes an iterable which is used to fill the heap.
    compare can be used to change how the heap is sorted. It should
    return True when the first value is sorted in comparison to the
    second value. By default this works like less than (i.e., this is
    a min heap by default).
    """
    def __init__(self, iterable=None, compare=lambda x, y: x < y):
        """Initiate the heap."""
        self.heap = []
        self.compare = compare
        if iterable:
            for value in iterable:
                self.push(value)

    def __repr__(self):
        """Return string representation of binary heap."""
        return str(self.heap)

    def swap(self, i1, i2):
        """Swap values at i1 and i2 in heap."""
        heap = self.heap
        heap[i1], heap[i2] = heap[i2], heap[i1]

    def push(self, x):
        """Push a value on to the heap and sort."""
        heap = self.heap
        heap.append(x)
        i = len(heap) - 1
        while i > 0:
            parent = _parent(i)
            if not self.compare(heap[i], heap[parent]):
                return
            self.swap(i, parent)
            i = parent

    def branch_sorted(self, i, branch):
        """Return whether branch of index i is sorted.

        i.e. in the proper position for pop.
        """
        try:
            return self.compare(self.heap[i], self.heap[branch])
        except IndexError:
            return False

    def is_sorted(self, i):
        """Return whether the value at heap[i] is sorted.

        i.e. in the proper position for pop.
        """
        left, right = _children(i)
        if right >= len(self.heap):
            return True
        return self.branch_sorted(i, left) and self.branch_sorted(i, right)

    def pop(self):
        """Pop the smallest value from the heap."""
        heap = self.heap
        value = heap[0]
        try:
            heap[0] = heap.pop()
        except IndexError:
            return value
        i = 0
        while i < (len(heap)) and not self.is_sorted(i):
            left, right = _children(i)
            to_swap = left if self.compare(heap[left], heap[right]) else right
            self.swap(i, to_swap)
            i = to_swap
        return value

    def valid(self, i=0):
        """Verify whether the current heap is valid.

        (According to the heap property.)"""
        heap = self.heap
        left, right = _children(i)
        if right >= len(heap):
            return True
        leftvalid = not self.compare(heap[left], heap[i])
        rightvalid = not self.compare(heap[right], heap[i])
        if not (leftvalid and rightvalid):
            return False
        return self.valid(left) and self.valid(right)
