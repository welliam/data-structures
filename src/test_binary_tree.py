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
    ([0, 2, 4, 3, 6, 8], -1),
]

R_ROT_TABLE = [
    ([2, 1], 1),
    ([2, 1, 3], 1),
    ([3, 2, 4, 1, 2.5, 3.5, 4.5], 2),
]

L_ROT_TABLE = [
    ([2, 3], 3),
    ([3, 3.5, 0, 3.3], 3.5),
    ([5, 1, 8, 0, 2, 7, 9, 6.5, 7.5], 8),
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
    t.asymmetrical_insert(1)
    assert t.contains(1)


def test_contains_deep():
    """Test insert stores original value when inserting new one."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.asymmetrical_insert(1)
    t.asymmetrical_insert(2)
    assert t.contains(1)


@pytest.mark.parametrize('to_insert, looking', CONTAINS_TABLE)
def test_contains(to_insert, looking):
    """Test contains method."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert t.contains(looking) == (looking in to_insert)


@pytest.mark.parametrize('to_insert', SIZE_TABLE)
def test_size(to_insert):
    """Test size method."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert t.size() == len(to_insert)


@pytest.mark.parametrize('to_insert, depth', DEPTH_TABLE)
def test_depth(to_insert, depth):
    """Assert depth for tree."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in to_insert:
        t.asymmetrical_insert(val)
    assert t.depth() == depth


@pytest.mark.parametrize('to_insert, balance', BALANCE_TABLE)
def test_balance(to_insert, balance):
    """Assert balance for tree."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in to_insert:
        t.asymmetrical_insert(val)
    assert t.balance() / (abs(t.balance()) or 1) == balance


@pytest.mark.parametrize('to_insert, equals', BREADTH_TABLE)
def test_breadth_first(to_insert, equals):
    """Test breadth first traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert list(t.breadth_first()) == equals


@pytest.mark.parametrize('to_insert, equals', PRE_TABLE)
def test_pre_order(to_insert, equals):
    """Test pre-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert list(t.pre_order()) == equals


@pytest.mark.parametrize('to_insert, equals', IN_ORDER_TABLE)
def test_in_order(to_insert, equals):
    """Test in-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert list(t.in_order()) == equals


@pytest.mark.parametrize('to_insert, equals', POST_ORDER_TABLE)
def test_post_order(to_insert, equals):
    """Test post-order traversal."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    assert list(t.post_order()) == equals


@pytest.mark.parametrize('to_insert, to_delete', DELETE_TABLE)
def test_delete(to_insert, to_delete):
    """Test deletion of a node."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in to_insert:
        t.asymmetrical_insert(value)
    t.delete(to_delete)
    assert not t.contains(to_delete)


@pytest.mark.parametrize('insert, delete, contains', DELETE_INTEGRITY_TABLE)
def test_delete_integrity(insert, delete, contains):
    """Test deletion of a node doesn't remove other values."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in insert:
        t.asymmetrical_insert(value)
    t.delete(delete)
    assert t.contains(contains)


@pytest.mark.parametrize('insert', FIND_MAX_TABLE)
def test_find_max(insert):
    """Test find_maxing node."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for value in insert:
        t.asymmetrical_insert(value)
    parent, max_node = t.root.find_max()
    assert max_node.value == max(insert)


def test_swap_left_top():
    """Test swapping swaps top value."""
    from .binary_tree import Node
    node = Node(0, Node(1))
    node.swap_left()
    assert node.value == 1


def test_swap_left_top_deep():
    """Test swapping swaps top value in deep swap."""
    from .binary_tree import Node
    node = Node(0, Node(1, Node(2)))
    node.swap_left()
    assert node.value == 1


def test_delete_nonexistent_node():
    """Test deleting when tree has no root"""
    from .binary_tree import BinaryTree
    with pytest.raises(KeyError):
        BinaryTree().delete(0)


def test_delete_nonexistent_node_deep():
    """Test deleting when value not in tree."""
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.asymmetrical_insert(0)
    with pytest.raises(KeyError):
        t.delete(1)


@pytest.mark.parametrize('tree, pivot', R_ROT_TABLE)
def test_rot_right_r(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)

    t.root.r_rot(set_child)
    assert t.root.value == pivot


@pytest.mark.parametrize('tree, pivot', R_ROT_TABLE)
def test_rot_integrity_contains_r(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)
    t.root.r_rot(set_child)

    for i in tree:
        assert t.contains(i)


@pytest.mark.parametrize('tree, pivot', R_ROT_TABLE)
def test_rot_integrity_size_r(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)
    t.root.r_rot(set_child)

    for i in tree:
        assert t.size() == len(tree)


@pytest.mark.parametrize('tree, pivot', L_ROT_TABLE)
def test_rot_left(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)

    t.root.l_rot(set_child)
    assert t.root.value == pivot


@pytest.mark.parametrize('tree, pivot', L_ROT_TABLE)
def test_rot_integrity_contains_l(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)
    t.root.l_rot(set_child)

    for i in tree:
        assert t.contains(i)


@pytest.mark.parametrize('tree, pivot', L_ROT_TABLE)
def test_rot_integrity_size_l(tree, pivot):
    from .binary_tree import BinaryTree

    def set_child(to):
        t.root = to

    t = BinaryTree()
    for i in tree:
        t.insert(i)
    t.root.l_rot(set_child)

    for i in tree:
        assert t.size() == len(tree)


def test_duplicate_insert():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(0)
    t.insert(0)
    assert t.size() == 1


def test_node_direction_right():
    from .binary_tree import Node
    assert Node(0).direction(Node(3)) == 'right'


def test_node_direction_left():
    from .binary_tree import Node
    assert Node(0).direction(Node(-3)) == 'left'


def test_node_path_rr():
    from .binary_tree import Node
    assert Node(0).path_direction(Node(3), Node(5)) == ('right', 'right')


def test_node_path_rl():
    from .binary_tree import Node
    assert Node(0).path_direction(Node(3), Node(1)) == ('right', 'left')


def test_node_path_ll():
    from .binary_tree import Node
    assert Node(0).path_direction(Node(-3), Node(-5)) == ('left', 'left')


def test_node_path_lr():
    from .binary_tree import Node
    assert Node(0).path_direction(Node(-3), Node(-1)) == ('left', 'right')


def test_node_l_rot_root_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(0)
    t.insert(2)

    def setchild(to):
        t.root = to
    t.root.l_rot(setchild)
    assert t.root.left.depth == 0


def test_node_l_rot_pivot_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(0)
    t.insert(2)

    def setchild(to):
        t.root = to
    t.root.l_rot(setchild)
    assert t.root.depth == 1


def test_node_r_rot_root_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(2)
    t.insert(0)

    def setchild(to):
        t.root = to
    t.root.r_rot(setchild)
    assert t.root.right.depth == 0


def test_node_r_rot_pivot_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    t.insert(2)
    t.insert(0)

    def setchild(to):
        t.root = to
    t.root.r_rot(setchild)
    assert t.root.depth == 1


def test_node_l_rot_complex_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        t.insert(val)

    def setchild(to):
        t.root.right = to
    t.root.right.l_rot(setchild)
    assert t.root.right.depth == 2


def test_node_r_rot_complex_depth():
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        t.insert(val)

    def setchild(to):
        t.root.left = to
    t.root.left.r_rot(setchild)
    assert t.root.left.depth == 2

REBALANCE_INSERT_TABLE = [
    ([3, 2, 1], [2, 1, 3]),
    ([1, 2, 3], [2, 1, 3]),
    ([1, 3, 2], [2, 1, 3]),
    ([3, 1, 2], [2, 1, 3]),

    ([0, 3, 2, 1], [2, 0, 3, 1]),
    ([0, 1, 2, 3], [1, 0, 2, 3]),
    ([0, 1, 3, 2], [1, 0, 3, 2]),
    ([0, 3, 1, 2], [1, 0, 3, 2]),

    ([5, 3, 7, 2, 1], [5, 2, 7, 1, 3]),
    ([5, 3, 7, 8, 9], [5, 3, 8, 7, 9]),

    ([5, 3, 7, 6, 8, 9], [7, 5, 8, 3, 6, 9]),
    ([5, 3, 7, 2, 4, 1], [3, 2, 5, 1, 4, 7]),
    ([5, 3, 8, 7, 9, 6], [7, 5, 8, 3, 6, 9]),
    ([5, 3, 8, 7, 9, 6], [7, 5, 8, 3, 6, 9]),
    ([5, 1, 7, 0, 2, 3], [2, 1, 5, 0, 3, 7]),

    ([50, 25, 75, 13, 32, 62, 80, 1, 0],
     [50, 25, 75, 1, 32, 62, 80, 0, 13]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9],
     [4, 2, 6, 1, 3, 5, 8, 7, 9])
]

@pytest.mark.parametrize('insert, breadth_first', REBALANCE_INSERT_TABLE)
def test_rebalance_insert(insert, breadth_first):
    from .binary_tree import BinaryTree
    t = BinaryTree()
    for i in insert:
        t.insert(i)
    assert list(t.breadth_first()) == breadth_first
