import pytest
from deque import Deque
from binary_heap import BinaryHeap
from priority_queue import PriorityQueue
from graph import Graph
from graf import Graf


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
def emptygraf():
    return Graf()


@pytest.fixture
def samplegraf():
    g = Graf()
    # c < - a - > b
    #       ^     |
    #       |     |
    #       d < - /
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'a')
    return g
