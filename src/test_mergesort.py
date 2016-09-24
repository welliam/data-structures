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


RUN_MERGE_TABLE = [
    ([0, 1], 1, [0, 1]),
    ([1, 0], 1, [0, 1]),
    ([1, 0, 7, 3, 8, 5], 1, [0, 1, 3, 7, 5, 8]),
    ([0, 1, 3, 7, 5, 8], 2, [0, 1, 3, 7, 5, 8]),
    ([0, 1, 3, 7, 5, 8], 4, [0, 1, 3, 5, 7, 8])
]


MERGE_LISTS = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [3, 210, 29, 284, 823, 82, 89129, 102, 2193, 91239, 123],
    [-5, 1, 3, 0, 1, 1, 1],
]


@pytest.mark.parametrize('t, start, middle, end', MERGE_LIST_INDICES)
def test_merge(t, start, middle, end):
    """Test merge."""
    from mergesort import merge
    merge(t, start, middle, end)
    part = t[start:end]
    assert part == sorted(part)


@pytest.mark.parametrize('t, step, expect', RUN_MERGE_TABLE)
def test_run_merge(t, step, expect):
    """Test an iteration of mergesort."""
    from mergesort import run_merge
    run_merge(t, step)
    assert t == expect


@pytest.mark.parametrize('t', MERGE_LISTS)
def test_mergesort(t):
    """Test sorting lists."""
    from mergesort import mergesort
    before = t[:]
    mergesort(t)
    assert t == sorted(before)
