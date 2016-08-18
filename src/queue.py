# -*- coding: utf-8 -*-

"""Implement queue abstract data type."""

from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Queue abstract data type."""

    def __init__(self, iterable=None):
        """Initialize the queue."""
        self.dll = DoublyLinkedList(iterable)

    def size(self):
        """Return the size of the queue."""
        return self.dll.count

    def enqueue(self, val):
        """Enqueue a value on the head of the queue."""
        self.push(val)

    def dequeue(self):
        """Pop a value off the tail of the queue."""
        return self.shift()

    def peek(self):
        """Return the value at the tail of the queue without removing it."""
        try:
            return self.dll.tail.value
        except AttributeError:
            raise IndexError("Peak called on empty stack.")
