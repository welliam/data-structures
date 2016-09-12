# -*- coding: utf-8 -*-

"""Implement directed graph abstract data type."""

from __future__ import print_function
from .stack import Stack
from .queue import Queue


class Graph(object):
    """Implement a directed graph."""

    def __init__(self):
        """Initialize a graph with no nodes or edges."""
        self._nodes = {}

    def add_node(self, n):
        """Add a node to the graph.

        Do nothing if it's already in the graph.
        """
        self._nodes.setdefault(n, {})

    def nodes(self):
        """Return a list of all nodes."""
        return list(self._nodes)

    def _edges(self):
        """Return a generator of all edges (represented by tuples)."""
        for node in self._nodes:
            for neighbor in self._nodes[node]:
                yield (node, neighbor, self._nodes[node][neighbor])

    def edges(self):
        """Return a list of all edges (represented by tuples).

        The tuples are generated like (node1, node2, weight).
        """
        return list(self._edges())

    def add_edge(self, a, b, weight):
        """Add an edge between two nodes.

        If those nodes don't exist yet in the graph, create them.
        """
        self.add_node(a)
        self.add_node(b)
        self._nodes[a][b] = weight

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
            try:
                del neighbors[n]
            except KeyError:
                pass

    def del_edge(self, a, b):
        """Delete an edge in the graph.

        Raises ValueError if the edge isn't in the graph.
        """
        try:
            del self._nodes[a][b]
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

    def shortest_path(self, start, end):
        """Dijkstra's algorithm."""
        distance_from_start = {start: 0}
        unvisited = set(self.nodes())
        parents = {}

        while end in unvisited:
            current = min((weight, node)
                          for node, weight
                          in distance_from_start.items()
                          if node in unvisited)[1]
            for neighbor in self.neighbors(current):
                weight = self._nodes[current][neighbor] + distance_from_start[current]
                dist = distance_from_start.setdefault(neighbor, weight)
                if weight <= dist:
                    distance_from_start[neighbor] = weight
                    parents[neighbor] = current
            unvisited.remove(current)

        s = []
        weight = 0
        current = end
        while current in parents:
            s.append(current)
            weight += self._nodes[parents[current]][current]
            current = parents[current]
        s.append(start)
        return s[::-1], weight


if __name__ == '__main__':
    g = Graph()
    g.add_edge('0-0', '1-0', 0)
    g.add_edge('0-0', '1-1', 0)
    g.add_edge('1-0', '2-0', 0)
    g.add_edge('1-0', '2-1', 0)
    g.add_edge('1-1', '2-2', 0)
    g.add_edge('1-1', '2-3', 0)
    print(r'''Graph:
         0-0
      /       \
   1-0         1-1
  /   \       /   \
2-0   2-1   2-2   2-3''')
    print('depth first   ', g.depth_first_traversal('0-0'))
    print('breadth first ', g.breadth_first_traversal('0-0'))
