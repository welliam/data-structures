import pytest

NODE_LABELS = [
    ['a'],
    ['a', 'b'],
    ['a', 'b', 'c', 'd']
]


def test_graph_nodes(empty_graph):
    """Test an empty graph has no nodes."""
    assert empty_graph.nodes() == []


def test_graph_edges(empty_graph):
    """Test an empty graph has no edges."""
    assert empty_graph.edges() == []


@pytest.mark.parametrize('labels', NODE_LABELS)
def test_add_node(empty_graph, labels):
    """Test adding some nodes means they're all in the graph."""
    for label in labels:
        empty_graph.add_node(label)
    assert all(map(lambda n: n in empty_graph.nodes(), labels))


def test_remove_edge_add(sample_graph):
    """Test deleting and readding an edge."""
    sample_graph.del_node('b')
    sample_graph.add_edge('a', 'b', 0)
    assert sample_graph.adjacent('a', 'b')


def test_add_edges(empty_graph):
    """Test adding an edge adds it to the result of edges()."""
    empty_graph.add_node('a')
    empty_graph.add_node('b')
    empty_graph.add_edge('a', 'b', 0)
    assert ('a', 'b', 0) in empty_graph.edges()


def test_add_edges_2(empty_graph):
    """Test adding two edges adds it to the result of edges()."""
    empty_graph.add_node('a')
    empty_graph.add_node('b')
    empty_graph.add_node('c')
    empty_graph.add_edge('a', 'b', 0)
    empty_graph.add_edge('a', 'c', 0)
    assert ('a', 'c', 0) in empty_graph.edges()


def test_add_edges_3(empty_graph):
    """Test only edges we explicitly add are in the graph."""
    empty_graph.add_node('a')
    empty_graph.add_node('b')
    empty_graph.add_node('c')
    empty_graph.add_edge('a', 'b', 0)
    empty_graph.add_edge('a', 'c', 0)
    assert ('b', 'c', 0) not in empty_graph.edges()


def test_add_edges_directed(empty_graph):
    """Test edges are added only in one direction."""
    empty_graph.add_node('a')
    empty_graph.add_node('b')
    empty_graph.add_edge('a', 'b', 0)
    assert ('b', 'a', 0) not in empty_graph.edges()


def test_add_edges_nonexistent_node_1(empty_graph):
    """Test adding an edge without the given nodes adds the first."""
    empty_graph.add_edge('a', 'b', 0)
    assert 'a' in empty_graph.nodes()


def test_add_edges_nonexistent_node_2(empty_graph):
    """Test adding an edge with the given nodes adds the second."""
    empty_graph.add_edge('a', 'b', 0)
    assert 'b' in empty_graph.nodes()


def test_add_edges_nonexistent_edge(empty_graph):
    """Test adding edges adds the edge.

    Even when those nodes are not already in the graph.
    """
    empty_graph.add_edge('a', 'b', 0)
    assert ('a', 'b', 0) in empty_graph.edges()


def test_delete_node(empty_graph):
    """Test deleting a node."""
    empty_graph.add_node('a')
    empty_graph.del_node('a')
    assert 'a' not in empty_graph.nodes()


def test_delete_node_edge(empty_graph):
    """Test deleting a node deletes its associated edges."""
    empty_graph.add_edge('a', 'b', 0)
    empty_graph.del_node('b')
    assert ('a', 'b') not in empty_graph.edges()


def test_delete_nonexistent_node(empty_graph):
    """Test deleting a nonexistent node raises ValueError."""
    with pytest.raises(ValueError):
        empty_graph.del_node('a')


def test_delete_edge(empty_graph):
    """Test deleting a node removes it from the result of edges()."""
    empty_graph.add_edge('a', 'b', 0)
    empty_graph.del_edge('a', 'b')
    assert ('a', 'b') not in empty_graph.edges()


def test_delete_nonexistent_edge(empty_graph):
    """Test deleting a nonexistent edge raises ValueError."""
    with pytest.raises(ValueError):
        empty_graph.del_edge('a', 'b')


def test_has_node(empty_graph):
    """Test adding a node means has_node returns True for it."""
    empty_graph.add_node('a')
    assert empty_graph.has_node('a')


def test_hasnt_node(empty_graph):
    """Test has_node doesn't return True regardless of input."""
    assert not empty_graph.has_node('a')


def test_neighbors_1(sample_graph):
    """Test b is a neighbor of a in sample graph."""
    assert 'b' in sample_graph.neighbors('a')


def test_neighbors_2(sample_graph):
    """Test d is a neighbor of b in sample graph."""
    assert 'd' in sample_graph.neighbors('b')


def test_neighbors_3(sample_graph):
    """Test c is a neighbor of a in sample graph."""
    assert 'c' in sample_graph.neighbors('a')


def test_neighbors_4(sample_graph):
    """Test d is not a neighbor of a in sample graph."""
    assert 'd' not in sample_graph.neighbors('a')


def test_neighbors_5(sample_graph):
    """Test b is not a neighbor of b in sample graph."""
    assert 'b' not in sample_graph.neighbors('b')


def test_adjacent_1(sample_graph):
    """Test a is adjacent to b in sample graph."""
    assert sample_graph.adjacent('a', 'b')


def test_adjacent_2(sample_graph):
    """Test b is adjacent to d in sample graph."""
    assert sample_graph.adjacent('b', 'd')


def test_adjacent_3(sample_graph):
    """Test d is adjacent to a in sample graph."""
    assert sample_graph.adjacent('d', 'a')


def test_not_adjacent(sample_graph):
    """Test a is adjacent to d in sample graph."""
    assert not sample_graph.adjacent('a', 'd')


def test_adjacent_error(empty_graph):
    """Test empty graph raises ValueError for adjacent."""
    with pytest.raises(ValueError):
        empty_graph.adjacent('a', 'b')


SAMPLE_WEIGHTS = [
    ('a', 'b', 3),
    ('b', 'c', 5),
    ('a', 'c', 10)
]


@pytest.fixture
def weighted_graph(empty_graph):
    for args in SAMPLE_WEIGHTS:
        empty_graph.add_edge(*args)
    return empty_graph


@pytest.mark.parametrize('n1, n2, w', SAMPLE_WEIGHTS)
def test_weights(weighted_graph, n1, n2, w):
    assert (n1, n2, w) in weighted_graph.edges()
