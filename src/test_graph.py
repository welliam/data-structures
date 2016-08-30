import pytest

NODE_LABELS = [
    ['a'],
    ['a', 'b'],
    ['a', 'b', 'c', 'd']
]


def test_graph_nodes(emptygraph):
    assert emptygraph.nodes() == []


def test_graph_edges(emptygraph):
    assert emptygraph.edges() == []


@pytest.mark.parametrize('labels', NODE_LABELS)
def test_add_node(emptygraph, labels):
    for label in labels:
        emptygraph.add_node(label)
    assert all(map(lambda n: n in emptygraph.nodes(), labels))

def test_remove_edge_add(samplegraph):
    samplegraph.del_node('b')
    samplegraph.add_edge('a', 'b', 0)
    assert samplegraph.adjacent('a', 'b')


def test_add_edges(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_edge('a', 'b', 0)
    assert ('a', 'b') in emptygraph.edges()


def test_add_edges_2(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_node('c')
    emptygraph.add_edge('a', 'b', 0)
    emptygraph.add_edge('a', 'c', 0)
    assert ('a', 'c') in emptygraph.edges()


def test_add_edges_3(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_node('c')
    emptygraph.add_edge('a', 'b', 0)
    emptygraph.add_edge('a', 'c', 0)
    assert ('b', 'c') not in emptygraph.edges()


def test_add_edges_directed(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_edge('a', 'b', 0)
    assert ('b', 'a') not in emptygraph.edges()


def test_add_edges_nonexistent_node_1(emptygraph):
    emptygraph.add_edge('a', 'b', 0)
    assert 'a' in emptygraph.nodes()


def test_add_edges_nonexistent_node_2(emptygraph):
    emptygraph.add_edge('a', 'b', 0)
    assert 'b' in emptygraph.nodes()


def test_add_edges_nonexistent_edge(emptygraph):
    emptygraph.add_edge('a', 'b', 0)
    assert ('a', 'b') in emptygraph.edges()


def test_delete_node(emptygraph):
    emptygraph.add_node('a')
    emptygraph.del_node('a')
    assert 'a' not in emptygraph.nodes()


def test_delete_node_edge(emptygraph):
    emptygraph.add_edge('a', 'b', 0)
    emptygraph.del_node('b')
    assert ('a', 'b') not in emptygraph.edges()


def test_delete_nonexistent_node(emptygraph):
    with pytest.raises(ValueError):
        emptygraph.del_node('a')


def test_delete_edge(emptygraph):
    emptygraph.add_edge('a', 'b', 0)
    emptygraph.del_edge('a', 'b', 0)
    assert ('a', 'b') not in emptygraph.edges()


def test_delete_nonexistent_edge(emptygraph):
    with pytest.raises(ValueError):
        emptygraph.del_edge('a', 'b', 0)


def test_has_node(emptygraph):
    emptygraph.add_node('a')
    assert emptygraph.has_node('a')


def test_hasnt_node(emptygraph):
    assert not emptygraph.has_node('a')


def test_neighbors_1(samplegraph):
    assert ('a', 'b') in samplegraph.neighbors('a')


def test_neighbors_2(samplegraph):
    assert ('b', 'd') in samplegraph.neighbors('b')


def test_neighbors_3(samplegraph):
    assert ('a', 'c') in samplegraph.neighbors('a')


def test_neighbors_4(samplegraph):
    assert ('a', 'd') not in samplegraph.neighbors('a')


def test_neighbors_5(samplegraph):
    assert ('d', 'b') not in samplegraph.neighbors('b')


def test_adjacent_1(samplegraph):
    assert samplegraph.adjacent('a', 'b')


def test_adjacent_2(samplegraph):
    assert samplegraph.adjacent('b', 'd')


def test_adjacent_3(samplegraph):
    assert samplegraph.adjacent('d', 'a')


def test_not_adjacent(samplegraph):
    assert not samplegraph.adjacent('a', 'd')


def test_adjacent_error(emptygraph):
    with pytest.raises(ValueError):
        emptygraph.adjacent('a', 'b')
