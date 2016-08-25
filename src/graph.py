class Graph(object):
    def __init__(self):
        self._nodes = set()
        self._edges = set()

    def add_node(self, n):
        if n not in self._nodes:
            self._nodes.add(n)

    def nodes(self):
        return list(self._nodes)

    def edges(self):
        return list(self._edges)

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self._edges.add((a, b))

    def del_node(self, n):
        try:
            self._nodes.remove(n)
            self._edges = set(filter(lambda p: n not in p, self._edges))
        except KeyError:
            raise ValueError('Node not in graph')

    def del_edge(self, a, b):
        try:
            self._edges.remove((a, b))
        except KeyError:
            raise ValueError('Node not in graph')

    def has_node(self, n):
        return n in self._nodes

    def neighbors(self, n):
        return filter(lambda p: p[0] == n, self._edges)

    def adjacent(self, n1, n2):
        if not (self.has_node(n1) or self.has_node(n2)):
            raise ValueError('Node not in graph')
        return (n1, n2) in self._edges
