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
