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
    pass
#     def __init__(self):
#         """Initialize binary tree."""
#         self.root = None
# 
#     def contains(self, val):
#         """Check whether val is contained in the tree."""
#         return self.root.value == val
# 
#     def insert(self, val):
#         """Insert a new value into the tree."""
#         if self.root is None:
#             self.root = Node(None, val, None)
#         current = self.root
#         while True:
#             if val < current.value:
#                 if current.left is None:
#                     current.left = 
#             else:
#                 # right branch
#                 pass
