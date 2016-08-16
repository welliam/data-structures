# -*- coding: utf-8 -*-

"""Test stack.py."""

import pytest


INIT_TABLE = [
    ([1, 2, 3], 3),
    ([2, 3], 3),
    ([3], 3)
]


@pytest.mark.parametrize('values, result', INIT_TABLE)
def test_init(values, result):
    """Test initialization of stack."""
    from stack import Stack
    stack = Stack(values)
    assert stack.pop() == result


def test_stack():
    """Test stack operations."""
    from stack import Stack
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2


def test_pop_error():
    """Test pop.

    Ensure that pop raises an IndexError when called upon an empty
    stack."""
    from stack import Stack
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
