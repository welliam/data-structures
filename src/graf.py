from functools import reduce


class Graf(object):
    def __init__(self):
        self._nodes = {}

    def add_node(self, n):
        self._nodes.setdefault(n, set())

    def nodes(self):
        return list(self._nodes)

    def edges(self):
        return reduce(
            lambda res, n: res + [(n, k) for k in self._nodes[n]],
            self._nodes,
            []
        )

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self._nodes[a].add(b)

    def del_node(self, n):
        try:
            del self._nodes[n]
        except KeyError:
            raise ValueError('Node not in graph')
        for neighbors in self._nodes.values():
            neighbors.discard(n)

    def del_edge(self, a, b):
        try:
            self._nodes[a].discard(b)
        except KeyError:
            raise ValueError('Node not in graph')

    def has_node(self, n):
        return n in self._nodes

    def neighbors(self, n):
        return list(self._nodes[n])

    def adjacent(self, n1, n2):
        try:
            return n2 in self._nodes[n1]
        except KeyError:
            raise ValueError('Node not in graph')
