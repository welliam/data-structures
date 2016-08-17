# -*- coding: utf-8 -*-

"""Test doubly_linked_list.py."""

def test_push():
    """Test push method."""
    from doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.push(0)
    assert lst.head.value == 0
    assert lst.tail.value == 0
    lst.push(1)
    assert lst.head.value == 1
    assert lst.tail.value == 0

def test_append():
    """Test append method."""
    from doubly_linked_list import DoublyLinkedList
    lst = DoublyLinkedList()
    lst.append(0)
    assert lst.tail.value == 0
    assert lst.head.value == 0
    lst.append(1)
    assert lst.tail.value == 1
    assert lst.head.value == 0
