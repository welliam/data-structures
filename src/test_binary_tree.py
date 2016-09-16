# -*- coding: utf-8 -*-

"""Test binary_tree.py ."""

import pytest


CONTAINS_TABLE = [
    (range(10), 3),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], 5),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], -100),
    ([4, 9, 7, 8, 1, 6, 0, 5, 2, 3], 100),
    ([1, 6, 9, 0, -10, .000001], 3)
]

DELETE_TABLE = [
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 1),
    ([1, 2], 1),
    ([2, 1], 2),
    ([5, 1, 7], 5),
    ([5, 1, 7], 5),
    ([5, 2, 7, 4], 5),

    ([5, 7, 2, 4, 3, 2.5], 5),

    ([10, 15, 5, 7, 4], 5),
    ([10, 15, 5, 2, 7, 4], 5),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5),

    ([20, 10, 15, 5, 7, 4], 5),
    ([20, 10, 15, 5, 2, 7, 4], 5),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5),

    ([0, 10, 15, 5, 7, 4], 5),
    ([0, 10, 15, 5, 2, 7, 4], 5),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5),
]

DELETE_INTEGRITY_TABLE = [
    ([1, 2], 2, 1),
    ([1, 2, 0], 2, 0),
    ([1, 2, 0], 2, 1),
    ([1, 2], 1, 2),
    ([1, 2, 3], 1, 2),
    ([5, 1, 7], 5, 1),
    ([5, 1, 7], 5, 7),

    ([5, 2, 7, 4], 5, 2),
    ([5, 2, 7, 4], 5, 7),
    ([5, 2, 7, 4], 5, 4),

    ([5, 7, 2, 4, 3, 2.5], 5, 7),
    ([5, 7, 2, 4, 3, 2.5], 5, 2),
    ([5, 7, 2, 4, 3, 2.5], 5, 4),
    ([5, 7, 2, 4, 3, 2.5], 5, 3),
    ([5, 7, 2, 4, 3, 2.5], 5, 2.5),

    ([10, 15, 5, 7, 4], 5, 10),
    ([10, 15, 5, 7, 4], 5, 15),
    ([10, 15, 5, 7, 4], 5, 7),
    ([10, 15, 5, 7, 4], 5, 4),

    ([10, 15, 5, 2, 7, 4], 5, 10),
    ([10, 15, 5, 2, 7, 4], 5, 15),
    ([10, 15, 5, 2, 7, 4], 5, 2),
    ([10, 15, 5, 2, 7, 4], 5, 7),
    ([10, 15, 5, 2, 7, 4], 5, 4),

    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 10),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 15),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 7),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 4),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 3),
    ([10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2.5),

    ([20, 10, 15, 5, 7, 4], 5, 10),
    ([20, 10, 15, 5, 7, 4], 5, 15),
    ([20, 10, 15, 5, 7, 4], 5, 7),
    ([20, 10, 15, 5, 7, 4], 5, 4),

    ([20, 10, 15, 5, 2, 7, 4], 5, 10),
    ([20, 10, 15, 5, 2, 7, 4], 5, 15),
    ([20, 10, 15, 5, 2, 7, 4], 5, 2),
    ([20, 10, 15, 5, 2, 7, 4], 5, 7),
    ([20, 10, 15, 5, 2, 7, 4], 5, 4),

    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 10),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 15),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 7),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 4),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 3),
    ([20, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2.5),

    ([0, 10, 15, 5, 7, 4], 5, 10),
    ([0, 10, 15, 5, 7, 4], 5, 15),
    ([0, 10, 15, 5, 7, 4], 5, 7),
    ([0, 10, 15, 5, 7, 4], 5, 4),

    ([0, 10, 15, 5, 2, 7, 4], 5, 10),
    ([0, 10, 15, 5, 2, 7, 4], 5, 15),
    ([0, 10, 15, 5, 2, 7, 4], 5, 2),
    ([0, 10, 15, 5, 2, 7, 4], 5, 7),
    ([0, 10, 15, 5, 2, 7, 4], 5, 4),

    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 10),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 15),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 7),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 4),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 3),
    ([0, 10, 15, 5, 2, 7, 4, 3, 2.5], 5, 2.5)
    
]

FIND_MAX_TABLE = [
    [1, 2],
    [1, 2, 0],
    range(500),
    [5, 4, 8, 2, 0, 1]
]

BREADTH_TABLE = [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 2, 3, 1, 4, 8, 6, 7, 9, 0], [5, 2, 8, 1, 3, 6, 9, 0, 4, 7]),
    ([10, 5, 15, 3, 8, 20, 4, 7, 6.5, 7.5],
     [10, 5, 15, 3, 8, 20, 4, 7, 6.5, 7.5])
]


PRE_TABLE = [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 2, 3, 1, 4, 8, 6, 7, 9, 0], [5, 2, 1, 0, 3, 4, 8, 6, 7, 9]),
    ([10, 5, 15, 3, 8, 20, 4, 7, 6.5, 7.5],
     [10, 5, 3, 4, 8, 7, 6.5, 7.5, 15, 20])
]


IN_ORDER_TABLE = [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 2, 3, 1, 4, 8, 6, 7, 9, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([10, 5, 15, 3, 8, 20, 4, 7, 6.5, 7.5],
     [3, 4, 5, 6.5, 7, 7.5, 8, 10, 15, 20])
]

POST_ORDER_TABLE = [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([5, 2, 3, 1, 4, 8, 6, 7, 9, 0],
     [0, 1, 4, 3, 2, 7, 6, 9, 8, 5]),
    ([10, 5, 15, 3, 8, 20, 4, 7, 6.5, 7.5],
     [4, 3, 6.5, 7.5, 7, 8, 5, 20, 15, 10])
]


SIZE_TABLE = [
    range(10),
    [4, 9, 7, 8, 1, 6, 0, 5, 2, 3],
    [4, 9, 7, 8, 1, 6, 0, 5, 2, 3],
    [4, 9, 7, 8, 1, 6, 0, 5, 2, 3],
    [1, 6, 9, 0, -10, .000001],
]


DEPTH_TABLE = [
    ([], 0),
    ([1], 1),
    (range(10), 10),
    (range(10, 0, -1), 10),
    ([5, 3, 7, 1, 6, 9], 3),
    ([0, 2, 4, 3, 6, 8], 5)
]


BALANCE_TABLE = [
    ([], 0),
    ([1], 0),
    (range(10), -1),
    (range(10, 0, -1), 1),
    ([5, 3, 7, 1, 6, 9], 0),
    ([0, 2, 4, 3, 6, 8], -1)
]


def test_node_value():
    """Test node stores value field."""
    from .binary_tree import Node
    assert Node(3, None, None).value == 3


def test_node_left():
    """Test node stores left branch field."""
    from .binary_tree import Node
    assert Node(None, 3, None).left == 3


def test_node_right():
    """Test node stores right branch field."""
    from .binary_tree import Node
    assert Node(None, None, 3).right == 3


def test_unary_node_value():
    """Test unary node constructor stores value."""
    from .binary_tree import Node
    assert Node(3).value == 3


def test_unary_node_left():
    """Test unary node constructor stores None as left branch."""
    from .binary_tree import Node
    assert Node(3).left is None


def test_unary_node_right():
    """Test unary node constructor stores None as right branch."""
    from .binary_tree import Node
    assert Node(3).right is None


def test_contains_basic():
    """Test contains single inserted value."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(1)
    assert t.contains(1)


def test_contains_deep():
    """Test insert stores original value when inserting new one."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(1)
    t.insert(2)
    assert t.contains(1)


@pytest.mark.parametrize('to_insert, looking', CONTAINS_TABLE)
def test_contains(to_insert, looking):
    """Test contains method."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert t.contains(looking) == (looking in to_insert)


@pytest.mark.parametrize('to_insert', SIZE_TABLE)
def test_size(to_insert):
    """Test size method."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert t.size() == len(to_insert)


@pytest.mark.parametrize('to_insert, depth', DEPTH_TABLE)
def test_depth(to_insert, depth):
    """Assert depth for tree."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in to_insert:
        t.insert(val)
    assert t.depth() == depth


@pytest.mark.parametrize('to_insert, balance', BALANCE_TABLE)
def test_balance(to_insert, balance):
    """Assert balance for tree."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in to_insert:
        t.insert(val)
    assert t.balance() / (abs(t.balance()) or 1) == balance


@pytest.mark.parametrize('to_insert, equals', BREADTH_TABLE)
def test_breadth_first(to_insert, equals):
    """Test breadth first traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert list(t.breadth_first()) == equals


@pytest.mark.parametrize('to_insert, equals', PRE_TABLE)
def test_pre_order(to_insert, equals):
    """Test pre-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert list(t.pre_order()) == equals


@pytest.mark.parametrize('to_insert, equals', IN_ORDER_TABLE)
def test_in_order(to_insert, equals):
    """Test in-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert list(t.in_order()) == equals


@pytest.mark.parametrize('to_insert, equals', POST_ORDER_TABLE)
def test_post_order(to_insert, equals):
    """Test post-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    assert list(t.post_order()) == equals


@pytest.mark.parametrize('to_insert, to_delete', DELETE_TABLE)
def test_delete(to_insert, to_delete):
    """Test deletion of a node."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.insert(value)
    t.delete(to_delete)
    assert not t.contains(to_delete)


@pytest.mark.parametrize('insert, delete, contains', DELETE_INTEGRITY_TABLE)
def test_delete_integrity(insert, delete, contains):
    """Test deletion of a node doesn't remove other values."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in insert:
        t.insert(value)
    t.delete(delete)
    assert t.contains(contains)


@pytest.mark.parametrize('insert', FIND_MAX_TABLE)
def test_find_max(insert):
    """Test find_maxing node."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in insert:
        t.insert(value)
    parent, max_node = t.root.find_max()
    assert max_node.value == max(insert)


def test_swap_left_top():
    from .binary_tree import Node
    node = Node(0, Node(1))
    node.swap_left()
    assert node.value == 1


def test_swap_left_top_deep():
    from .binary_tree import Node
    node = Node(0, Node(1, Node(2)))
    node.swap_left()
    assert node.value == 1
