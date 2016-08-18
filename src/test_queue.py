# -*- coding: utf-8 -*-

"""Test queue.py."""

import pytest

QUEUE_TABLE = [
    ([1, 2, 3], 1),
    ([1, 2], 1),
    ([1], 1)
]

@pytest.mark.parametrize('values, result', QUEUE_TABLE)
def test_dequeue(values, result):
    from queue import Queue
    assert Queue(values).dequeue() == result
