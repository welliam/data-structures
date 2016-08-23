import pytest
from deque import Deque
from binary_heap import BinaryHeap


@pytest.fixture
def emptydeque():
    return Deque()


@pytest.fixture
def emptyheap():
    return BinaryHeap()
