# -*- coding: utf-8 -*-

"""Test binary_tree.py"""

import pytest


CONTAINS_TABLE = [
    (range(10), 3),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], 5),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], -100),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], 100),
    ([1, 6, 9, 0, -10, .000001], 3),
]


def test_node_value():
    from binary_tree import Node
    assert Node(3, None, None).value == 3


def test_node_left():
    from binary_tree import Node
    assert Node(None, 3, None).left == 3


def test_node_right():
    from binary_tree import Node
    assert Node(None, None, 3).right == 3


def test_unary_node_value():
    from binary_tree import Node
    assert Node(3).value == 3


def test_unary_node_left():
    from binary_tree import Node
    assert Node(3).left is None


def test_unary_node_right():
    from binary_tree import Node
    assert Node(3).right is None


def test_contains_basic():
    from binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(1)
    assert t.contains(1)


def test_contains_deep():    
    from binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(1)
    t.insert(2)
    assert t.contains(1)


@pytest.mark.parametrize('to_insert, looking', CONTAINS_TABLE)
def test_contains(to_insert, looking):
    from binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert t.contains(looking) == (looking in to_insert)
