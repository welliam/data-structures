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
        if self.root is None:
            self.root = Node(val)
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
