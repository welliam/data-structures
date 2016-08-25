# -*- coding: utf-8 -*-

"Test priority queue functionality."""

import pytest
from priority_queue import _Prioritized, PriorityQueue

ITERABLES = [
    [1, 2, 3, 4, 5],
    [],
    [9, 9, 9, 9, 9]
]

def test_prioritized_comparison():
    assert not (_Prioritized(2, 1, 0) < _Prioritized(1, 0, 1))


def test_prioritized_order():
    assert _Prioritized(2, 0, 0) < _Prioritized(1, 0, 1)


def test_basic_pushpop(emptypqueue):
    emptypqueue.insert(0, 5)
    assert emptypqueue.pop() == 0


def test_basic_priority_1(emptypqueue):
    emptypqueue.insert(0, 0)
    emptypqueue.insert('notme', 1)
    assert emptypqueue.pop() == 0


def test_basic_priority_2(emptypqueue):
    """Test priority queue gives highest priority value."""
    emptypqueue.insert('notme', 1)
    emptypqueue.insert(0, 0)
    assert emptypqueue.pop() == 0


@pytest.mark.parametrize('iterable', ITERABLES)
def test_priority(iterable):
    """Test priority queue gives highest priority value."""
    pq = PriorityQueue()
    for value in iterable:
        pq.insert(value, 1)
    pq.insert(0, 0)
    assert pq.pop() == 0


def test_peek_failure(emptypqueue):
    """Test empty priority queue raises IndexError when peeked."""
    with pytest.raises(IndexError):
        emptypqueue.peek()


def test_pop_failure(emptypqueue):
    """Test empty priority queue raises IndexError when popped."""
    with pytest.raises(IndexError):
        emptypqueue.pop()


def test_priority_pops(emptypqueue):
    """Test priority queue pops values in proper order."""
    emptypqueue.insert(2, 2)
    emptypqueue.insert(5, 5)
    emptypqueue.insert(4, 4)
    emptypqueue.insert(1, 1)
    emptypqueue.insert(3, 3)
    results = []
    try:
        while True:
            results.append(emptypqueue.pop())
    except IndexError:
        assert results == sorted(results)


def test_queue_1(emptypqueue):
    emptypqueue.insert(1, 0)
    emptypqueue.insert(2, 0)
    emptypqueue.insert(3, 0)
    assert emptypqueue.pop() == 1


def test_queue_2(emptypqueue):
    emptypqueue.insert(1, 0)
    emptypqueue.insert(2, 0)
    emptypqueue.insert(3, 0)
    emptypqueue.pop()
    assert emptypqueue.pop() == 2


def test_queue_3(emptypqueue):
    emptypqueue.insert(1, 0)
    emptypqueue.insert(2, 0)
    emptypqueue.insert(3, 0)
    emptypqueue.pop()
    emptypqueue.pop()
    assert emptypqueue.pop() == 3


def test_queue_4(emptypqueue):
    emptypqueue.insert(1, 0)
    emptypqueue.insert(2, 0)
    emptypqueue.insert(3, 0)
    for _ in range(20):
        emptypqueue.insert(False, 1)
    emptypqueue.pop()
    emptypqueue.pop()
    assert emptypqueue.pop() == 3
