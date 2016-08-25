import pytest

NODE_LABELS = [
    ['a'],
    ['a', 'b'],
    ['a', 'b', 'c', 'd']
]


def test_graf_nodes(emptygraf):
    assert emptygraf.nodes() == []


def test_graf_edges(emptygraf):
    assert emptygraf.edges() == []


@pytest.mark.parametrize('labels', NODE_LABELS)
def test_add_node(emptygraf, labels):
    for label in labels:
        emptygraf.add_node(label)
    assert all(map(lambda n: n in emptygraf.nodes(), labels))


def test_remove_edge_add(samplegraf):
    samplegraf.del_node('b')
    samplegraf.add_edge('a', 'b')
    assert samplegraf.adjacent('a', 'b')


def test_add_edges(emptygraf):
    emptygraf.add_node('a')
    emptygraf.add_node('b')
    emptygraf.add_edge('a', 'b')
    assert ('a', 'b') in emptygraf.edges()


def test_add_edges_2(emptygraf):
    emptygraf.add_node('a')
    emptygraf.add_node('b')
    emptygraf.add_node('c')
    emptygraf.add_edge('a', 'b')
    emptygraf.add_edge('a', 'c')
    assert ('a', 'c') in emptygraf.edges()


def test_add_edges_3(emptygraf):
    emptygraf.add_node('a')
    emptygraf.add_node('b')
    emptygraf.add_node('c')
    emptygraf.add_edge('a', 'b')
    emptygraf.add_edge('a', 'c')
    assert ('b', 'c') not in emptygraf.edges()


def test_add_edges_directed(emptygraf):
    emptygraf.add_node('a')
    emptygraf.add_node('b')
    emptygraf.add_edge('a', 'b')
    assert ('b', 'a') not in emptygraf.edges()


def test_add_edges_nonexistent_node_1(emptygraf):
    emptygraf.add_edge('a', 'b')
    assert 'a' in emptygraf.nodes()


def test_add_edges_nonexistent_node_2(emptygraf):
    emptygraf.add_edge('a', 'b')
    assert 'b' in emptygraf.nodes()


def test_add_edges_nonexistent_edge(emptygraf):
    emptygraf.add_edge('a', 'b')
    assert ('a', 'b') in emptygraf.edges()


def test_delete_node(emptygraf):
    emptygraf.add_node('a')
    emptygraf.del_node('a')
    assert 'a' not in emptygraf.nodes()


def test_delete_node_edge(emptygraf):
    emptygraf.add_edge('a', 'b')
    emptygraf.del_node('b')
    assert ('a', 'b') not in emptygraf.edges()


def test_delete_nonexistent_node(emptygraf):
    with pytest.raises(ValueError):
        emptygraf.del_node('a')


def test_delete_edge(emptygraf):
    emptygraf.add_edge('a', 'b')
    emptygraf.del_edge('a', 'b')
    assert ('a', 'b') not in emptygraf.edges()


def test_delete_nonexistent_edge(emptygraf):
    with pytest.raises(ValueError):
        emptygraf.del_edge('a', 'b')


def test_has_node(emptygraf):
    emptygraf.add_node('a')
    assert emptygraf.has_node('a')


def test_hasnt_node(emptygraf):
    assert not emptygraf.has_node('a')


def test_neighbors_1(samplegraf):
    assert 'b' in samplegraf.neighbors('a')


def test_neighbors_2(samplegraf):
    assert 'd' in samplegraf.neighbors('b')


def test_neighbors_3(samplegraf):
    assert 'c' in samplegraf.neighbors('a')


def test_neighbors_4(samplegraf):
    assert 'd' not in samplegraf.neighbors('a')


def test_neighbors_5(samplegraf):
    assert 'b' not in samplegraf.neighbors('b')


def test_adjacent_1(samplegraf):
    assert samplegraf.adjacent('a', 'b')


def test_adjacent_2(samplegraf):
    assert samplegraf.adjacent('b', 'd')


def test_adjacent_3(samplegraf):
    assert samplegraf.adjacent('d', 'a')


def test_not_adjacent(samplegraf):
    assert not samplegraf.adjacent('a', 'd')


def test_adjacent_error(emptygraf):
    with pytest.raises(ValueError):
        emptygraf.adjacent('a', 'b')
