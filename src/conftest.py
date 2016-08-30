import pytest
from .deque import Deque
from .binary_heap import BinaryHeap
from .priority_queue import PriorityQueue
from .graph import Graph
from .adjacency_list import AdjacencyList


@pytest.fixture
def emptydeque():
    return Deque()


@pytest.fixture
def emptyheap():
    return BinaryHeap()


@pytest.fixture
def emptypqueue():
    return PriorityQueue()


@pytest.fixture
def emptygraph():
    return Graph()


@pytest.fixture
def samplegraph():
    g = Graph()
    # c < - a - > b
    #       ^     |
    #       |     |
    #       d < - /
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'a')
    return g


@pytest.fixture
def empty_adjacency_list():
    return AdjacencyList()


@pytest.fixture
def sample_adjacency_list():
    g = AdjacencyList()
    # c < - a - > b
    #       ^     |
    #       |     |
    #       d < - /
    g.add_edge('a', 'b', 0)
    g.add_edge('a', 'c', 0)
    g.add_edge('b', 'd', 0)
    g.add_edge('d', 'a', 0)
    return g
