import pytest
from .deque import Deque
from .binary_heap import BinaryHeap
from .priority_queue import PriorityQueue
from .graph import Graph


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
def empty_graph():
    return Graph()


@pytest.fixture
def sample_graph():
    g = Graph()
    # c < - a - > b
    #       ^     |
    #       |     |
    #       d < - /
    g.add_edge('a', 'b', 0)
    g.add_edge('a', 'c', 0)
    g.add_edge('b', 'd', 0)
    g.add_edge('d', 'a', 0)
    return g
