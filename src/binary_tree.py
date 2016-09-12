# -*- coding: utf-8 -*-

"""Implement a binary tree."""


class Node(object):
    """Node for binary tree."""
    def __init__(self, left, value, right):
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
        return self.root.value == val

    def insert(self, val):
        """Insert a new value into the tree."""
        self.root = Node(None, val, None)
