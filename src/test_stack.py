# -*- coding: utf-8 -*-

import pytest

INIT_TABLE = [
    ([1, 2, 3], 3),
    ([2, 3], 3),
    ([3], 3)
]


@pytest.mark.parametrize('values, result', INIT_TABLE)
def test_init(values, result):
    from stack import Stack
    stack = Stack(values)
    assert stack.pop() == result


def test_stack():
    from stack import Stack
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2


def test_pop_error():
    from stack import Stack
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
