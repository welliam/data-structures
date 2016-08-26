# -*- coding: utf-8 -*-

"""Implement queue abstract data type."""

from .doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Queue abstract data type."""

    def __init__(self, iterable=None):
        """Initialize the queue."""
        self.dll = DoublyLinkedList(iterable)

    def __repr__(self):
        """Return string representation of Queue."""
        return self.dll.display()

    def size(self):
        """Return the size of the queue."""
        return self.dll.count

    def enqueue(self, val):
        """Enqueue a value on the head of the queue."""
        self.dll.push(val)

    def dequeue(self):
        """Pop a value off the tail of the queue."""
        try:
            return self.dll.shift()
        except IndexError:
            raise IndexError("dequeue called on empty queue.")

    def peek(self):
        """Return the value at the tail of the queue without removing it."""
        try:
            return self.dll.tail.value
        except AttributeError:
            return None
