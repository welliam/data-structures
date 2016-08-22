import pytest
from deque import Deque

@pytest.fixture
def emptydeque():
    return Deque()
