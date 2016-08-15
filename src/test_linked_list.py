# -*- coding: utf-8 -*-

import pytest


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


def test_pop_error():
    from linked_list import LinkedList
    with pytest.raises(IndexError) as e_info:
        lst = LinkedList()
        lst.pop()


def test_size():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    assert lst.size() == 3
    
