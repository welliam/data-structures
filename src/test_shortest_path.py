import pytest

from .graph import Graph


START = 'start'
END = 'end'


SHORTEST_PATH_TABLE = [
    (([START, END], 0), [(START, END, 0)]),
    (([START, 'a', END], 10), [
        (START, 'a', 5),
        ('a', END, 5),
        (START, END, 20)
    ]),
    (([START, 'b', 'e', END], 20), [
        (START, 'a', 7),
        (START, 'b', 9),
        (START, 'e', 14),
        ('a', 'b', 10),
        ('a', 'c', 15),
        ('b', 'c', 11),
        ('b', 'e', 2),
        ('c', END, 6),
        ('e', END, 9)
    ]),
]


@pytest.mark.parametrize('result, edges', SHORTEST_PATH_TABLE)
def test_shortest_path(edges, result):
    "Test shortest path algorithm"""
    g = Graph()
    for edge in edges:
        g.add_edge(*edge)
    assert g.shortest_path(START, END) == result
