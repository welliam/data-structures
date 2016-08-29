# -*- coding: utf-8 -*-

"""Implement deque abstract data type."""

from .doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Implement a Deque"""

    def __init__(self, iterable=None):
        """Initialize the deque."""
        self.dll = DoublyLinkedList(iterable)

    def __repr__(self):
        """Returnstring representation of deque."""
        return self.dll.display()

    def size(self):
        """Return the size of the deque."""
        return self.dll.count

    def append(self, val):
        """Append a value on the head of the deque."""
        self.dll.append(val)

    def appendleft(self, val):
        """Append a value on the tail of the deque."""
        self.dll.push(val)

    def pop(self):
        """Pop a value off the tail of the deque."""
        return self.dll.shift()

    def popleft(self):
        """Pop a value off the head of the deque."""
        return self.dll.pop()

    def peek(self):
        """Return self.tail."""
        try:
            return self.dll.tail.value
        except AttributeError:
            return None

    def peekleft(self):
        """Return self.head."""
        try:
            return self.dll.head.value
        except AttributeError:
            return None
