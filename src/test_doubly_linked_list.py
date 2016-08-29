# -*- coding: utf-8 -*-

"""Test doubly_linked_list.py."""

import pytest


REMOVE_ERROR_NUMBERS = [[1, 2, 3], [1], []]


def test_push():
    """Test push method."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.push(0)
    assert lst.head.value == 0
    assert lst.tail.value == 0
    lst.push(1)
    assert lst.head.value == 1
    assert lst.tail.value == 0


def test_append():
    """Test append method."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.append(0)
    assert lst.tail.value == 0
    assert lst.head.value == 0
    lst.append(1)
    assert lst.tail.value == 1
    assert lst.head.value == 0


def test_pop():
    """Test pop method."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.push(1)
    lst.push(2)
    assert lst.count == 2
    assert lst.pop() == 2
    assert lst.pop() == 1
    assert lst.count == 0


def test_pop_error():
    """Test pop throws IndexError."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.pop()


def test_shift():
    """Test shift method."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.append(1)
    lst.append(2)
    assert lst.count == 2
    assert lst.shift() == 2
    assert lst.shift() == 1
    assert lst.count == 0


def test_shift_error():
    """Test shift throws IndexError."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.shift()


def test_remove():
    """Test remove method."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.push(3)
    lst.push(2)
    lst.push(1)
    lst.remove(2)
    assert lst.head.next_node.value == 3
    assert lst.tail.previous_node.value == 1
    lst.remove(1)
    assert lst.head.value == 3
    lst.remove(3)
    assert lst.head is None
    assert lst.tail is None


@pytest.mark.parametrize('values', REMOVE_ERROR_NUMBERS)
def test_remove_error(values):
    """Test remove throws IndexError."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList(values)
    with pytest.raises(IndexError):
        lst.remove(False)


def test_append_and_pop():
    """Test combination of append and pop operations."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList([3, 2, 1])
    assert lst.pop() == 1
    assert lst.pop() == 2
    lst.append(4)
    assert lst.pop() == 3
    assert lst.pop() == 4


def test_push_and_shift():
    """Test combination of shift and push operations."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList([1, 2, 3])
    assert lst.shift() == 1
    assert lst.shift() == 2
    lst.push(4)
    assert lst.shift() == 3
    assert lst.shift() == 4


def test_size_remove():
    """Test combination of shift and push operations."""
    from .doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList([1, 2, 3])
    lst.remove(2)
    assert lst.size() == 2
    lst.remove(3)
    assert lst.size() == 1
    lst.remove(1)
    assert lst.size() == 0
