# -*- coding: utf-8 -*-

"""Implement a binary tree."""


class Node(object):
    """Node for binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize node with given values."""
        self.left = left
        self.value = value
        self.right = right


class BinaryTree(object):

    """Binary tree."""
    def __init__(self):
        """Initialize binary tree."""
        self.root = None
        self._length = 0

    def contains(self, val):
        """Check whether val is contained in the tree."""
        current = self.root
        while current is not None:
            if current.value == val:
                return True
            if val < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def insert(self, val):
        """Insert a new value into the tree."""
        self._length += 1
        if self.root is None:
            self.root = Node(val)
            return
        current = self.root
        while True:
            if val < current.value:
                if current.left is None:
                    current.left = Node(val)
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    return
                else:
                    current = current.right

    def size(self):
        """Return the size of the BinaryTree."""
        return self._length

    def _depth(self, node):
         """Static method to recursively compute the depth of the node."""
         if node is None:
             return 0
         else:
             return (max(self._depth(node.left), self._depth(node.right)) + 1)
 
     def depth(self):
         """Return the depth of the tree."""
         return self._depth(self.root)
