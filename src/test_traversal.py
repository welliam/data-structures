'''Test traversal of adjacency_list.py.'''

import pytest
from .adjacency_list import AdjacencyList


@pytest.fixture
def self_looped():
    g = AdjacencyList()
    g.add_edge('a', 'a', 0)
    return g


# The following fixtures for graphs have two associated variables:
# <NAME>_DEPTH and <NAME>_BREADTH
# which are lists of tuples of two values. The second of which must
# come after the first when the test is being run with the proper
# traversal method for the variable started at 'a'

def comesbefore(t, a, b):
    """Used in testing traversal methods.

    Because which branch we traverse first is not guaranteed (or
    relevant), we can't test simple equality on the output of
    traversal methods-- this method is used instead."""
    return b in t[t.index(a):]


@pytest.fixture
def simple():
    """A simple, non-looped graph."""
    g = AdjacencyList()
    g.add_edge('a', 'b', 0)
    g.add_edge('b', 'c', 0)
    g.add_edge('b', 'd', 0)
    return g

SIMPLE_DEPTH = [('a', 'b'), ('b', 'c'), ('b', 'd')]
SIMPLE_BREADTH = SIMPLE_DEPTH  # same in this case


@pytest.fixture
def complex():
    """A graph with a non-self referential loop."""
    g = AdjacencyList()
    g.add_edge('a', 'b', 0)
    g.add_edge('b', 'c', 0)
    g.add_edge('c', 'a', 0)
    g.add_edge('a', 'dead end', 0)
    return g

COMPLEX_DEPTH = [('a', 'b'), ('b', 'c'), ('a', 'dead end')]
COMPLEX_BREADTH = [('a', 'b'), ('b', 'c'), ('dead end', 'c')]


@pytest.fixture
def complex_2():
    """A complex graph with multiple loops."""
    g = AdjacencyList()
    g.add_edge('a', 'b', 0)
    g.add_edge('b', 'c', 0)
    g.add_edge('c', 'a', 0)
    g.add_edge('c', 'b', 0)
    g.add_edge('a', 'dead end', 0)
    return g

# the same variables as for complex are relevant


@pytest.fixture
def tree():
    """A graph which resembles a binary tree."""
    g = AdjacencyList()
    g.add_edge('0-0', '1-0', 0)
    g.add_edge('0-0', '1-1', 0)
    g.add_edge('1-0', '2-0', 0)
    g.add_edge('1-0', '2-1', 0)
    g.add_edge('1-1', '2-2', 0)
    g.add_edge('1-1', '2-3', 0)
    return g

TREE_DEPTH = [
    ('0-0', '1-0'),
    ('1-0', '2-0'),
    ('1-0', '2-1'),
    ('0-0', '1-1'),
    ('1-1', '2-2'),
    ('1-1', '2-3')
]

TREE_BREADTH = [
    ('0-0', '1-0'),
    ('0-0', '1-1'),
    ('1-0', '2-0'),
    ('1-0', '2-1'),
    ('1-0', '2-2'),
    ('1-0', '2-3'),
    ('1-1', '2-0'),
    ('1-1', '2-1'),
    ('1-1', '2-2'),
    ('1-1', '2-3')
]


# depth first


def test_depth_traversal_empty(self_looped):
    """Test that depth first traversal throws error on an absent node."""
    with pytest.raises(KeyError):
        self_looped.depth_first_traversal('b')


def test_depth_traversal_self_looped(self_looped):
    """Test that depth first traversal is traversing at all."""
    assert self_looped.depth_first_traversal('a') == ['a']


@pytest.mark.parametrize('a, b', SIMPLE_DEPTH)
def test_depth_traversal_simple(simple, a, b):
    """Test that depth first traverses a nonlooped graph."""
    assert comesbefore(simple.depth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', COMPLEX_DEPTH)
def test_depth_traversal_complex(complex, a, b):
    """Test that depth first traverses a more complex looped graph."""
    assert comesbefore(complex.depth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', COMPLEX_DEPTH)
def test_depth_traversal_complex_2(complex_2, a, b):
    """Test that depth first traverses an even more complex graph."""
    assert comesbefore(complex_2.depth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', TREE_DEPTH)
def test_depth_traversal_tree(tree, a, b):
    """Test that depth first traverses an even more complex graph."""
    assert comesbefore(tree.depth_first_traversal('0-0'), a, b)


# breadth first


def test_breadth_traversal_empty(self_looped):
    """Test that breadth first traversal throws error on an absent node."""
    with pytest.raises(KeyError):
        self_looped.breadth_first_traversal('b')


def test_breadth_traversal_self_looped(self_looped):
    """Test that breadth first traversal is traversing at all."""
    assert self_looped.breadth_first_traversal('a') == ['a']


@pytest.mark.parametrize('a, b', SIMPLE_BREADTH)
def test_breadth_traversal_simple(simple, a, b):
    """Test that breadth first traverses a nonlooped graph."""
    assert comesbefore(simple.breadth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', COMPLEX_BREADTH)
def test_breadth_traversal_complex(complex, a, b):
    """Test that breadth first traverses a more complex looped graph."""
    assert comesbefore(complex.breadth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', COMPLEX_BREADTH)
def test_breadth_traversal_complex_2(complex_2, a, b):
    """Test that breadth first traverses an even more complex graph."""
    assert comesbefore(complex_2.breadth_first_traversal('a'), a, b)


@pytest.mark.parametrize('a, b', TREE_BREADTH)
def test_breadth_traversal_tree(tree, a, b):
    """Test that breadth first traverses an even more complex graph."""
    assert comesbefore(tree.breadth_first_traversal('0-0'), a, b)
