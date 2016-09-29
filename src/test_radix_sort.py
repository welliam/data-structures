import pytest


RADIX_SORT_LISTS = [
    [],
    [1],
    [1, 2],
    [2, 1],
    range(100),
    range(100, 0, -1),
]


@pytest.mark.parametrize('lst', RADIX_SORT_LISTS)
def test_radix_sort(lst):
    """Test radix sort sorts input."""
    from radix_sort import radix_sort
    assert radix_sort(lst) == sorted(lst)
