# -*- coding: utf-8 -*-

import pytest


def test_push():
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(0)
    assert lst.head.value == 0 
