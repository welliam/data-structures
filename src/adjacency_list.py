# -*- coding: utf-8 -*-

"""Implement directed graph abstract data type."""

from functools import reduce
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

    def _depth_first_traversal_rec(self, start, res):
        """Recur through the depth first search."""
        if start in res:
            return res
        res.append(start)
        for node in self.neighbors(start):
            res = self._depth_first_traversal_rec(node, res)
        return res

    def depth_first_traversal(self, start):
        """Return a list of nodes as found in depth-first order."""
        return self._depth_first_traversal_rec(start, [])

    def breadth_first_traversal(self, start):
        """Return a list of nodes as found in breadth-first order."""
        queue = Queue()
        queue.enqueue(start)
        result = []
        while queue.size():
            root = queue.dequeue()
            if root not in result:
                result.append(root)
                for node in self.neighbors(root):
                    queue.enqueue(node)
        return result
