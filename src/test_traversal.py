'''Test traversal of adjacency_list.py.'''

import pytest
from .adjacency_list import AdjacencyList


@pytest.fixture
def self_looped():
    g = AdjacencyList()
    g.add_edge('a', 'a')
    return g


@pytest.fixture
def simple():
    """A simple, non-looped graph."""
    g = AdjacencyList()
    g.add_edge('a', 'a')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    return g


@pytest.fixture
def complex():
    """A graph with a non-self referential loop."""
    g = AdjacencyList()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('a', 'dead end')
    return g


@pytest.fixture
def complex_2():
    """A complex graph with multiple loops."""
    g = AdjacencyList()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('b', 'c')
    g.add_edge('a', 'dead end')
    return g


@pytest.fixture
def tree():
    """A graph which resembles a binary tree."""
    g = AdjacencyList()
    g.add_edge('0-0', '1-0')
    g.add_edge('0-0', '1-1')
    g.add_edge('1-0', '2-0')
    g.add_edge('1-0', '2-1')
    g.add_edge('1-1', '2-3')
    g.add_edge('1-1', '2-4')
    return g


# depth first


def test_depth_traversal_simple(self_looped):
    """Test that depth first traversal is traversing at all."""
    assert self_looped.depth_first_traversal('a') == ['a']


def test_depth_traversal_empty(self_looped):
    """Test that depth first traversal is [] when on an absent node."""
    assert self_looped.depth_first_traversal('b') == []
