# -*- coding: utf-8 -*-

"""Test binary_tree.py"""


def test_contains():
    from binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(1)
    assert t.contains(1)


def test_node_value():
    from binary_tree import Node
    assert Node(None, 3, None).value == 3


def test_node_left():
    from binary_tree import Node
    assert Node(3, None, None).left == 3


def test_node_right():
    from binary_tree import Node
    assert Node(None, None, 3).right == 3
