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
