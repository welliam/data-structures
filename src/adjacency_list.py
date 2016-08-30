# -*- coding: utf-8 -*-

"""Implement directed graph abstract data type."""

from __future__ import print_function
from functools import reduce
from .stack import Stack
from .queue import Queue


class AdjacencyList(object):
    """Implement a directed graph."""

    def __init__(self):
        """Initialize a graph with no nodes or edges."""
        self._nodes = {}

    def add_node(self, n):
        """Add a node to the graph.

        Do nothing if it's already in the graph.
        """
        self._nodes.setdefault(n, set())

    def nodes(self):
        """Return a list of all nodes."""
        return list(self._nodes)

    def edges(self):
        """Return a list of all edges (represented by tuples)."""
        return reduce(
            lambda res, n: res + [(n, k) for k in self._nodes[n]],
            self._nodes,
            []
        )

    def add_edge(self, a, b):
        """Add an edge between two nodes.

        If those nodes don't exist yet in the graph, create them.
        """
        self.add_node(a)
        self.add_node(b)
        self._nodes[a].add(b)

    def del_node(self, n):
        """Delete a node in the graph.

        Deletes all the edges involving the node as well.  Raises
        ValueError if the node isn't in the graph.
        """
        try:
            del self._nodes[n]
        except KeyError:
            raise ValueError('Node not in graph')
        for neighbors in self._nodes.values():
            neighbors.discard(n)

    def del_edge(self, a, b):
        """Delete an edge in the graph.

        Raises ValueError if the edge isn't in the graph.
        """
        try:
            self._nodes[a].discard(b)
        except KeyError:
            raise ValueError('Node not in graph')

    def has_node(self, n):
        """Return whether a node is in the graph."""
        return n in self._nodes

    def neighbors(self, n):
        """Return a list of all the neighbors a node has."""
        return list(self._nodes[n])

    def adjacent(self, n1, n2):
        """Return whether two nodes are adjacent.

        Raises a ValueError if either node is not in the graph.
        """
        try:
            return n2 in self._nodes[n1]
        except KeyError:
            raise ValueError('Node not in graph')

    def _traverse(self, start, nonempty, add, remove):
        """Traverse iteratively.

        Uses given functions (nonempty, add, remove) to store
        nodes. Depending on the behavior of these functions, this
        traversal may be performed differently.
        """
        add(start)
        result = []
        while nonempty():
            root = remove()
            if root not in result:
                result.append(root)
                for node in self.neighbors(root):
                    add(node)
        return result

    def depth_first_traversal(self, start):
        """Return a list of nodes as found in depth-first order."""
        stack = Stack()
        return self._traverse(start, stack.size, stack.push, stack.pop)

    def breadth_first_traversal(self, start):
        """Return a list of nodes as found in breadth-first order."""
        queue = Queue()
        return self._traverse(start, queue.size, queue.enqueue, queue.dequeue)


if __name__ == '__main__':
    g = AdjacencyList()
    g.add_edge('0-0', '1-0')
    g.add_edge('0-0', '1-1')
    g.add_edge('1-0', '2-0')
    g.add_edge('1-0', '2-1')
    g.add_edge('1-1', '2-2')
    g.add_edge('1-1', '2-3')
    print(r'''Graph:
         0-0
      /       \
   1-0         1-1
  /   \       /   \
2-0   2-1   2-2   2-3''')
    print('depth first   ', g.depth_first_traversal('0-0'))
    print('breadth first ', g.breadth_first_traversal('0-0'))
