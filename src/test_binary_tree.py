# -*- coding: utf-8 -*-

"""Test binary_tree.py"""


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


def test_contains():
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
