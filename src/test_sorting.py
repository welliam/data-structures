# -*- coding: utf-8 -*-

"""Test sorting.py."""

import pytest

LIST_TABLE = [
    ([x for x in range(0, 10)], [x for x in range(0, 10)]),
    ([x for x in range(10, 0, -1)], [x for x in range(1, 11)]),
    ([5, 1, 4, 2, 3, 7, 6, 9, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([], [])
]


@pytest.mark.parametrize('list_in, list_out', LIST_TABLE)
def test_insertion_sort(list_in, list_out):
    from .sorting import insertion_sort
    print(list_in)
    assert list_out == insertion_sort(list_in)
