class Graph(object):
    def __init__(self):
        self._nodes = []
        self._edges = []

    def add_node(self, n):
        if n not in self._nodes:
            self._nodes.append(n)

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self._edges.append((a, b))

    def del_node(self, n):
        try:
            self._nodes.remove(n)
            self._edges = filter(lambda p: n not in p, self._edges)
        except ValueError:
            raise ValueError('Node not in graph')

    def del_edge(self, a, b):
        try:
            self._edges.remove((a, b))
        except ValueError:
            raise ValueError('Node not in graph')

    def has_node(self, n):
        return n in self._nodes

    def neighbors(self, n):
        return filter(lambda p: p[0] == n, self._edges)
