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
        self.add_node(a)
        self._edges.append((a, b))
