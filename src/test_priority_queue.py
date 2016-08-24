# -*- coding: utf-8 -*-

"Test priority queue functionality."""

import pytest
from priority_queue import PriorityQueue

ITERABLES = [
    [1, 2, 3, 4, 5],
    [],
    [9, 9, 9, 9, 9]
]


def test_basic_pushpop(emptypqueue):
    emptypqueue.insert(0, 5)
    assert emptypqueue.pop() == 0


def test_basic_priority_1(emptypqueue):
    emptypqueue.insert(0, 0)
    emptypqueue.insert('notme', 1)
    assert emptypqueue.pop() == 0


def test_basic_priority_2(emptypqueue):
    emptypqueue.insert('notme', 1)
    emptypqueue.insert(0, 0)
    assert emptypqueue.pop() == 0


@pytest.mark.parametrize('iterable', ITERABLES)
def test_priority(iterable):
    pq = PriorityQueue()
    for value in iterable:
        pq.insert(value, 1)
    pq.insert(0, 0)
    assert pq.pop() == 0


def test_peek_failure(emptypqueue):
    with pytest.raises(IndexError):
        emptypqueue.peek()


def test_pop_failure(emptypqueue):
    with pytest.raises(IndexError):
        emptypqueue.pop()
