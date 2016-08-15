# -*- coding: utf-8 -*-

import pytest


SEARCH_TABLE = [
    (5, 5)
]

DISPLAY_TABLE = [
    ([5, 4, 3], u'(3, 4, 5)'),
    ([5], u'(5)'),
    ([], u'()')
]


def test_push():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(0)
    assert lst.head.value == 0


def test_pop():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(0)
    assert lst.pop() == 0


def test_constructor():
    from linked_list import LinkedList
    lst = LinkedList([1, 2, 3])
    assert lst.pop() == 3
    assert lst.pop() == 2
    assert lst.pop() == 1


def test_pop_error():
    from linked_list import LinkedList
    with pytest.raises(IndexError):
        lst = LinkedList()
        lst.pop()


def test_size():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    assert lst.size() == 3


@pytest.mark.parametrize('val, result', SEARCH_TABLE)
def test_search(val, result):
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(val)
    assert val == lst.search(5).value


def test_remove():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(5)
    lst.remove(lst.search(5))
    assert lst.search(5) is None


@pytest.mark.parametrize('values, result', DISPLAY_TABLE)
def test_display(values, result):
    from linked_list import LinkedList
    lst = LinkedList()
    for val in values:
        lst.push(val)
    assert lst.display() == result
