# -*- coding: utf-8 -*-

"""Implement stack abstract data type."""

import linked_list


class Stack():
    """Stack abstract data type."""

    def __init__(self, iterable=None):
        """Initialize the stack.

        Fills it with values from iterable if provided."""
        self.linked_list = linked_list.LinkedList()
        linked_list.LinkedList.__init__(self.linked_list, iterable)

    def push(self, val):
        """Push value onto the stack."""
        self.linked_list.push(val)

    def pop(self):
        """Pop value from stack."""
        return self.linked_list.pop()
