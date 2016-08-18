# -*- coding: utf-8 -*-

"""Test linked_list.py."""

import pytest


SEARCH_TABLE = [
    (5, [5], 5),
    (5, [5, 4, 3, 2, 1], 5)
]

DISPLAY_TABLE = [
    ([5, 4, 3], u'(3, 4, 5)'),
    ([5], u'(5)'),
    ([], u'()')
]


def test_push():
    """Test push method."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(0)
    assert lst.head.value == 0


def test_pop():
    """Test pop method."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(0)
    assert lst.pop() == 0


def test_pop_error():
    """Test that pop called on an empty list raises an IndexError."""
    from linked_list import LinkedList
    with pytest.raises(IndexError):
        lst = LinkedList()
        lst.pop()


def test_constructor():
    """Test __init__ method."""
    from linked_list import LinkedList
    lst = LinkedList([1, 2, 3])
    assert lst.pop() == 3
    assert lst.pop() == 2
    assert lst.pop() == 1


def test_size():
    """Test size method."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    assert lst.size() == 3


@pytest.mark.parametrize('looking, values, result', SEARCH_TABLE)
def test_search(looking, values, result):
    """Test search method."""
    from linked_list import LinkedList
    lst = LinkedList()
    for val in values:
        lst.push(val)
    assert looking == lst.search(looking).value


def test_search_not_found():
    """Test that searching and not finding a value in the list returns
    None.
    """
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.search(0) is None


def test_remove_1():
    """Test remove method."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(5)
    lst.remove(lst.search(5))
    assert lst.search(5) is None


def test_remove_2():
    """Test remove method."""
    from linked_list import LinkedList
    lst = LinkedList([5, 1, 2, 3, 4])
    lst.remove(lst.search(5))
    assert lst.search(5) is None


def test_remove_error():
    """Test that remove raises IndexError when value is not in list."""
    from linked_list import Node, LinkedList
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.remove(Node(1, None))


@pytest.mark.parametrize('values, result', DISPLAY_TABLE)
def test_display(values, result):
    """Test display method."""
    from linked_list import LinkedList
    lst = LinkedList()
    for val in values:
        lst.push(val)
    assert lst.display() == result
