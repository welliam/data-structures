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


class TaggedInt(int):
    def __new__(cls, val, tag=''):
        obj = int.__new__(cls, val)
        obj.val = val
        obj.tag = tag
        return obj

    def __repr__(self):
        if self.tag:
            return 'TaggedInt({}, {})'.format(self.val, self.tag)
        else:
            return 'TaggedInt({})'.format(self.val)


MERGE_LISTS = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [3, 210, 29, 284, 823, 82, 89129, 102, 2193, 91239, 123],
    [-5, 1, 3, 0, 1, 1, 1],
]

STABILITY_TEST_LISTS = [
    [
        TaggedInt(0),
        TaggedInt(3, 'before'),
        TaggedInt(3, 'after'),
        TaggedInt(9),
        TaggedInt(-5)
    ], [
        TaggedInt(3, 'before'),
        TaggedInt(3, 'after'),
    ], [
        TaggedInt(7),
        TaggedInt(3, 'before'),
        TaggedInt(5),
        TaggedInt(9),
        TaggedInt(3, 'after'),
    ], [
        TaggedInt(9),
        TaggedInt(3, 'before'),
        TaggedInt(3, 'after'),
    ], [
        TaggedInt(3, 'before'),
        TaggedInt(3, 'after'),
        TaggedInt(0)
    ]
]


@pytest.mark.parametrize('t, start, middle, end', MERGE_LIST_INDICES)
def test_merge(t, start, middle, end):
    """Test merge."""
    from .mergesort import merge
    merge(t, start, middle, end)
    part = t[start:end]
    assert part == sorted(part)


@pytest.mark.parametrize('t, step, expect', RUN_MERGE_TABLE)
def test_run_merge(t, step, expect):
    """Test an iteration of mergesort."""
    from .mergesort import run_merge
    run_merge(t, step)
    assert t == expect


@pytest.mark.parametrize('t', MERGE_LISTS)
def test_mergesort(t):
    """Test sorting lists."""
    from .mergesort import mergesort
    before = t[:]
    mergesort(t)
    assert t == sorted(before)


@pytest.mark.parametrize('lst', STABILITY_TEST_LISTS)
def test_mergesort_stability(lst):
    """Test sorting lists."""
    from .mergesort import mergesort
    mergesort(lst)
    lst = [t.tag for t in lst]
    assert 'after' in lst[lst.index('before'):]
