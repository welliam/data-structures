import pytest


MERGE_LIST_INDICES = [
    ([1, 2], 0, 1, 2),
    ([2, 1], 0, 1, 2),
    ([1, 3, 5, 2, 6, 8, -50], 0, 3, 6),
    ([1, 3, 5, 2, 6, 8, -50], 1, 3, 6),
    ([1, 3, 5, 2, 6, 8, -50], 1, 3, 5),
    ([1, 3, 5, 2, 6, 8, -50], 2, 3, 5),
    ([1, 3, 5, 2, 6, 8, -50], 2, 3, 4),
]


@pytest.mark.parametrize('t, start, middle, end', MERGE_LIST_INDICES)
def test_merge(t, start, middle, end):
    from mergesort import merge
    merge(t, start, middle, end)
    part = t[start:end]
    assert part == sorted(part)
