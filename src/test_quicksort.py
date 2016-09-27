"""Test file for the quicksort algorithm."""
import pytest

TEST_LISTS = [
    [1],
    [1, 2],
    [0, 5, 2, 4, 3],
    [6, 3, 2, 4, 1, 7, 9, 8, 0],
    list('asldkfjaskdfjalkdjflkasvanwlerru13muctp2mucmog')
]


@pytest.mark.parametrize('array', TEST_LISTS)
def test_partition_less(array):
    from .quicksort import partition
    array = array[:]
    index = partition(array, 0, len(array))
    try:
        hi = max(array[:index])
    except ValueError:
        hi = float('-inf')
    assert hi <= array[index]


@pytest.mark.parametrize('array', TEST_LISTS)
def test_partition_greater(array):
    from .quicksort import partition
    array = array[:]
    index = partition(array, 0, len(array))
    try:
        lo = min(array[index + 1:])
    except ValueError:
        lo = float('+inf')
    assert lo >= array[index]
