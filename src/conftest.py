import pytest
from deque import Deque
from binary_heap import BinaryHeap
from priority_queue import PriorityQueue


@pytest.fixture
def emptydeque():
    return Deque()


@pytest.fixture
def emptyheap():
    return BinaryHeap()

@pytest.fixture
def emptypqueue():
    return PriorityQueue()
