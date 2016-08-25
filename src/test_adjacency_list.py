import pytest

NODE_LABELS = [
    ['a'],
    ['a', 'b'],
    ['a', 'b', 'c', 'd']
]


def test_adjacency_list_nodes(empty_adjacency_list):
    assert empty_adjacency_list.nodes() == []


def test_adjacency_list_edges(empty_adjacency_list):
    assert empty_adjacency_list.edges() == []


@pytest.mark.parametrize('labels', NODE_LABELS)
def test_add_node(empty_adjacency_list, labels):
    for label in labels:
        empty_adjacency_list.add_node(label)
    assert all(map(lambda n: n in empty_adjacency_list.nodes(), labels))


def test_remove_edge_add(sample_adjacency_list):
    sample_adjacency_list.del_node('b')
    sample_adjacency_list.add_edge('a', 'b')
    assert sample_adjacency_list.adjacent('a', 'b')


def test_add_edges(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    empty_adjacency_list.add_node('b')
    empty_adjacency_list.add_edge('a', 'b')
    assert ('a', 'b') in empty_adjacency_list.edges()


def test_add_edges_2(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    empty_adjacency_list.add_node('b')
    empty_adjacency_list.add_node('c')
    empty_adjacency_list.add_edge('a', 'b')
    empty_adjacency_list.add_edge('a', 'c')
    assert ('a', 'c') in empty_adjacency_list.edges()


def test_add_edges_3(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    empty_adjacency_list.add_node('b')
    empty_adjacency_list.add_node('c')
    empty_adjacency_list.add_edge('a', 'b')
    empty_adjacency_list.add_edge('a', 'c')
    assert ('b', 'c') not in empty_adjacency_list.edges()


def test_add_edges_directed(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    empty_adjacency_list.add_node('b')
    empty_adjacency_list.add_edge('a', 'b')
    assert ('b', 'a') not in empty_adjacency_list.edges()


def test_add_edges_nonexistent_node_1(empty_adjacency_list):
    empty_adjacency_list.add_edge('a', 'b')
    assert 'a' in empty_adjacency_list.nodes()


def test_add_edges_nonexistent_node_2(empty_adjacency_list):
    empty_adjacency_list.add_edge('a', 'b')
    assert 'b' in empty_adjacency_list.nodes()


def test_add_edges_nonexistent_edge(empty_adjacency_list):
    empty_adjacency_list.add_edge('a', 'b')
    assert ('a', 'b') in empty_adjacency_list.edges()


def test_delete_node(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    empty_adjacency_list.del_node('a')
    assert 'a' not in empty_adjacency_list.nodes()


def test_delete_node_edge(empty_adjacency_list):
    empty_adjacency_list.add_edge('a', 'b')
    empty_adjacency_list.del_node('b')
    assert ('a', 'b') not in empty_adjacency_list.edges()


def test_delete_nonexistent_node(empty_adjacency_list):
    with pytest.raises(ValueError):
        empty_adjacency_list.del_node('a')


def test_delete_edge(empty_adjacency_list):
    empty_adjacency_list.add_edge('a', 'b')
    empty_adjacency_list.del_edge('a', 'b')
    assert ('a', 'b') not in empty_adjacency_list.edges()


def test_delete_nonexistent_edge(empty_adjacency_list):
    with pytest.raises(ValueError):
        empty_adjacency_list.del_edge('a', 'b')


def test_has_node(empty_adjacency_list):
    empty_adjacency_list.add_node('a')
    assert empty_adjacency_list.has_node('a')


def test_hasnt_node(empty_adjacency_list):
    assert not empty_adjacency_list.has_node('a')


def test_neighbors_1(sample_adjacency_list):
    assert 'b' in sample_adjacency_list.neighbors('a')


def test_neighbors_2(sample_adjacency_list):
    assert 'd' in sample_adjacency_list.neighbors('b')


def test_neighbors_3(sample_adjacency_list):
    assert 'c' in sample_adjacency_list.neighbors('a')


def test_neighbors_4(sample_adjacency_list):
    assert 'd' not in sample_adjacency_list.neighbors('a')


def test_neighbors_5(sample_adjacency_list):
    assert 'b' not in sample_adjacency_list.neighbors('b')


def test_adjacent_1(sample_adjacency_list):
    assert sample_adjacency_list.adjacent('a', 'b')


def test_adjacent_2(sample_adjacency_list):
    assert sample_adjacency_list.adjacent('b', 'd')


def test_adjacent_3(sample_adjacency_list):
    assert sample_adjacency_list.adjacent('d', 'a')


def test_not_adjacent(sample_adjacency_list):
    assert not sample_adjacency_list.adjacent('a', 'd')


def test_adjacent_error(empty_adjacency_list):
    with pytest.raises(ValueError):
        empty_adjacency_list.adjacent('a', 'b')
