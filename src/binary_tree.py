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

    def find_max(self):
        """Find the parent of the largest node in this node's branches."""
        parent = None
        while self.right:
            parent = self
            self = self.right
        return parent, self

    def swap_left(self):
        while self.left:
            self.value, self.left.value = self.left.value, self.value
            parent = self
            self = self.left
        parent.left = None
        return self

    def r_rot(self, setchild):
        pivot = self.left
        pivot_r = pivot.right

        pivot.right = self
        self.left = pivot_r
        setchild(pivot)

    def l_rot(self, setchild):
        pivot = self.right
        pivot_l = pivot.left

        pivot.left = self
        self.right = pivot_l
        setchild(pivot)

    def reset_depth(self):
        """Reset depth of node according to its children."""
        self.depth = 1 + max(
            self.left.depth if self.left else 0,
            self.right.depth if self.right else 0
        )


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

    @staticmethod
    def _walk_path(path):
        while path:
            path.pop().reset_depth()

    def insert(self, val):
        """Insert a new value into the tree."""
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            path = []
            while True:
                path.append(current)
                if val == current.value:
                    return
                branch = 'left' if val < current.value else 'right'
                if getattr(current, branch) is None:
                    setattr(current, branch, Node(val))
                    break
                else:
                    current = getattr(current, branch)
            self._walk_path(path)
        self._length += 1

    def _remove_root(self, root):
        """Remove node at root."""
        if root.left and root.right:
            parent, max_node = root.left.find_max()
            root.value = max_node.value
            if parent is None:
                root.left = None
            elif max_node.left is None:
                parent.right = None
            else:
                max_node.swap_left()
        else:
            self.root = root.left if root.left else root.right

    def delete(self, val):
        """Delete a node from the tree while optimizing tree balance."""
        if self.root is None:
            raise KeyError('Value not found in tree.')
        parent = self.root
        if parent.value == val:
            return self._remove_root(self.root)
        while True:
            branch_name = 'left' if val < parent.value else 'right'
            branch = getattr(parent, branch_name)
            if not branch:
                raise KeyError('Value not found in tree.')
            if branch.value == val:
                if branch.left and branch.right:
                    self._remove_root(branch)
                else:
                    to_set = branch.left if branch.left else branch.right
                    setattr(parent, branch_name, to_set)
                break
            parent = branch

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
