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


def test_add_edges(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_edge('a', 'b')
    assert ('a', 'b') in emptygraph.edges()


def test_add_edges_2(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_node('c')
    emptygraph.add_edge('a', 'b')
    emptygraph.add_edge('a', 'c')
    assert ('a', 'c') in emptygraph.edges()


def test_add_edges_3(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_node('c')
    emptygraph.add_edge('a', 'b')
    emptygraph.add_edge('a', 'c')
    assert ('b', 'c') not in emptygraph.edges()


def test_add_edges_directed(emptygraph):
    emptygraph.add_node('a')
    emptygraph.add_node('b')
    emptygraph.add_edge('a', 'b')
    assert ('b', 'a') not in emptygraph.edges()


def test_add_edges_nonexistent_node_1(emptygraph):
    emptygraph.add_edge('a', 'b')
    assert 'a' in emptygraph.nodes()


def test_add_edges_nonexistent_node_2(emptygraph):
    emptygraph.add_edge('a', 'b')
    assert 'b' in emptygraph.nodes()


def test_add_edges_nonexistent_edge(emptygraph):
    emptygraph.add_edge('a', 'b')
    assert ('a', 'b') in emptygraph.edges()


def test_delete_node(emptygraph):
    emptygraph.add_node('a')
    emptygraph.del_node('a')
    assert 'a' not in emptygraph.nodes()


def test_delete_node_edge(emptygraph):
    emptygraph.add_edge('a', 'b')
    emptygraph.del_node('b')
    assert ('a', 'b') not in emptygraph.edges()


def test_delete_nonexistent_node(emptygraph):
    with pytest.raises(ValueError):
        emptygraph.del_node('a')


def test_delete_edge(emptygraph):
    emptygraph.add_edge('a', 'b')
    emptygraph.del_edge('a', 'b')
    assert ('a', 'b') not in emptygraph.edges()


def test_delete_nonexistent_edge(emptygraph):
    with pytest.raises(ValueError):
        emptygraph.del_edge('a', 'b')
