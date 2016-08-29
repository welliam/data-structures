# -*- coding: utf-8 -*-

"""Implement stack abstract data type."""

from .linked_list import LinkedList


class Stack(object):
    """Stack abstract data type."""

    def __init__(self, iterable=None):
        """Initialize the stack.

        Fills it with values from iterable if provided."""
        self.linked_list = LinkedList(iterable)

    def __len__(self):
        return self.linked_list.count

    def push(self, val):
        """Push value onto the stack."""
        self.linked_list.push(val)

    def pop(self):
        """Pop value from stack."""
        return self.linked_list.pop()

    def peek(self):
        """Return top of stack without popping the value."""
        try:
            return self.linked_list.head.value
        except AttributeError:
            raise IndexError('Cannot peek on empty stack.')
