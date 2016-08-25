class Graph(object):
    def __init__(self):
        self._nodes = []
        self._edges = []

    def add_node(self, n):
        self._nodes.append(n)

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges
