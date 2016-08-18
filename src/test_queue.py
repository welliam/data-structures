# -*- coding: utf-8 -*-

"""Test queue.py."""

import pytest

DEQUEUE_TABLE = [
    ([1, 2, 3], 1),
    ([1, 2], 1),
    ([1], 1)
]


SIZE_TABLE = [[1, 2, 3], [1, 2], [1]]


@pytest.mark.parametrize('values, result', DEQUEUE_TABLE)
def test_dequeue(values, result):
    from queue import Queue
    assert Queue(values).dequeue() == result


@pytest.mark.parametrize('values', SIZE_TABLE)
def test_size(values):
    from queue import Queue
    assert Queue(values).size() == len(values)


def test_enqueue():
    from queue import Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3


def test_peek():
    from queue import Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    assert q.size() == 3
    q.dequeue()
    assert q.peek() == 2
