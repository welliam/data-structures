# -*- coding: utf-8 -*-


"""Implement linked list abstract data type."""


class Node(object):
    """Node internally by LinkedList to chain values."""

    def __init__(self, value, next_node):
        """Create a node containing value and pointing to next_node."""
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    """Create a linked list object."""

    def __init__(self, iterable=None):
        """Initialize LinkedList."""
        self.head = None
        self.count = 0
        if iterable is not None:
            for value in iterable:
                self.push(value)

    def push(self, val):
        """Push val onto the linked list."""
        self.head = Node(val, self.head)
        self.count += 1

    def pop(self):
        """Pop a value from the linked list and return it. Throw
        IndexError if list is empty.
        """
        if not self.head:
            raise IndexError('Linked list is empty.')
        self.count -= 1
        popped = self.head.value
        self.head = self.head.next_node
        return popped

    def size(self):
        """Return the current size the list."""
        return self.count

    def search(self, val):
        """Search the list for val; if found, return the node
        containing that value, otherwise return None.
        """
        current_node = self.head
        while current_node:
            if current_node.value == val:
                return current_node
            current_node = current_node.next_node

    def remove(self, node):
        """Remove node from the list if found. Otherwise raise
        IndexError.
        """
        if self.head == node:
            self.head = self.head.next_node
            return
        elif self.count > 0:
            current_node = self.head
            while current_node.next_node:
                print(current_node.value)
                if current_node.next_node == node:
                    current_node.next_node = current_node.next_node.next_node
                    self.count -= 1
                    return
                else:
                    current_node = current_node.next_node
        raise IndexError('Linked list does not contain node.')

    def display(self):
        """Return a string representation of the linked list."""
        if self.count == 0:
            return u'()'
        else:
            current_node = self.head.next_node
            result = u'({}'.format(self.head.value)
            while current_node:
                result += u', {}'.format(current_node.value)
                current_node = current_node.next_node
            return result + u')'
