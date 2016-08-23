# -*- coding: utf-8 -*-

"""Test queue.py."""

import pytest

DEQUEUE_TABLE = [
    ([1, 2, 3], 1),
    ([1, 2], 1),
    ([1], 1)
]


LEN_QUEUE_TABLE = [
    ([1, 2, 3], 0),
    ([1, 2, 3], 1),
    ([1, 2, 3], 3),
    ([2, 3], 2),
    ([], 0)
]


SIZE_TABLE = [[1, 2, 3], [1, 2], [1]]


@pytest.mark.parametrize('values, result', DEQUEUE_TABLE)
def test_dequeue(values, result):
    """Test dequeue method of queue."""
    from queue import Queue
    assert Queue(values).dequeue() == result


@pytest.mark.parametrize('values', SIZE_TABLE)
def test_size(values):
    """Test size method of queue."""
    from queue import Queue
    assert Queue(values).size() == len(values)


def test_enqueue():
    """Test enqueue method of queue."""
    from queue import Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.dll.tail.value == 1
    assert q.dll.head.value == 3


def test_peek():
    """Test peek method of queue."""
    from queue import Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    assert q.size() == 3


def test_empty_peek():
    """Test that peek returns None when queue is empty."""
    from queue import Queue
    assert Queue().peek() is None


def test_dequeue_error():
    """Test dequeue raises IndexError when queue is empty."""
    from queue import Queue
    with pytest.raises(IndexError):
        Queue().dequeue()


@pytest.mark.parametrize('values', SIZE_TABLE)
def test_size_enqueue(values):
    """Test size works with enqueue."""
    from queue import Queue
    s = Queue()
    for value in values:
        s.enqueue(value)
    assert s.size() == len(values)


@pytest.mark.parametrize('values, dequeue', LEN_QUEUE_TABLE)
def test_size_dequeue(values, dequeue):
    """Test size works with dequeue."""
    from queue import Queue
    s = Queue(values)
    for i in range(dequeue):
        s.dequeue()
    assert s.size() == len(values) - dequeue


@pytest.mark.parametrize('values, dequeue', LEN_QUEUE_TABLE)
def test_len_queue(values, dequeue):
    """Test size for many queue operations"""
    from queue import Queue
    s = Queue()
    for value in values:
        print(s)
        s.enqueue(value)
    for i in range(dequeue):
        s.dequeue()
    assert s.size() == len(values) - dequeue
