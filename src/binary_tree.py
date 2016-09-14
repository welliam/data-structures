# -*- coding: utf-8 -*-

"""Implement a binary tree."""
from src.queue import Queue
from src.stack import Stack


class Node(object):
    """Node for binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize node with given values."""
        self.left = left
        self.value = value
        self.right = right
        self.depth = 0


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
        path = []
        while True:
            path.append(current)
            if val < current.value:
                if current.left is None:
                    current.left = Node(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    break
                else:
                    current = current.right
        while path:
            n = path.pop()
            n.depth = 1 + max(
                0 if not n.left else n.left.depth,
                0 if not n.right else n.right.depth
            )

    def size(self):
        """Return the size of the BinaryTree."""
        return self._length

    def _depth(self, node):
        """Static method to recursively compute the depth of the node."""
        return 0 if not node else node.depth + 1

    def depth(self):
        """Return the depth of the tree."""
        return self._depth(self.root)

    def balance(self):
        """Return the balance of the tree.

        1 is left deep, 0 is balanced, and -1 is right deep.
        """
        if self.root is None:
            return 0
        return self._depth(self.root.left) - self._depth(self.root.right)

    def _traverse(self, add, remove, nonempty):
        """Traverse the graph depth of breadth first.

        Depending on the behavior of add, remove and nonempty.
        Depth-first traversal would be pre-order."""
        while nonempty():
            current = remove()
            if current is not None:
                yield current.value
                add(current.left, current.right)

    def breadth_first(self):
        """Return the list from a breadth-first traversal.

        We start with the left branch of each node for each level.
        """
        queue = Queue()

        def add(a, b):
            queue.enqueue(a)
            queue.enqueue(b)
        queue.enqueue(self.root)
        return self._traverse(add, queue.dequeue, queue.size)

    def pre_order(self):
        """Return the elements pre-order depth-first."""
        stack = Stack()

        def add(a, b):
            stack.push(b)
            stack.push(a)
        stack.push(self.root)
        return self._traverse(add, stack.pop, stack.size)

    def in_order(self):
        """Return the elements in-order depth-first."""
        to_process = Stack()
        current = self.root
        while True:
            if current:
                to_process.push(current)
                current = current.left
            elif to_process.size():
                popped = to_process.pop()
                yield popped.value
                current = popped.right
            else:
                break

    def post_order(self):
        """Return the elements post-order depth-first."""
        to_process = Stack()
        current = self.root
        traversed = set()
        if self.root is not None:
            while True:
                if current.left and current.left not in traversed:
                    to_process.push(current)
                    current = current.left
                elif current.right and current.right not in traversed:
                    to_process.push(current)
                    current = current.right
                else:
                    yield current.value
                    traversed.add(current)
                    if to_process.size():
                        current = to_process.pop()
                    else:
                        break