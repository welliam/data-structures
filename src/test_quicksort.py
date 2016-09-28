"""Test file for the quicksort algorithm."""
import pytest

TEST_LISTS = [
    [1],
    [1, 2],
    [2, 1],
    [0, 5, 2, 4, 3],
    [1, 0, 2],
    #[6, 3, 2, 4, 1, 7, 9, 8, 0],
    #list('asldkfjaskdfjalkdjflkasvanwlerru13muctp2mucmog')
]


@pytest.mark.parametrize('array', TEST_LISTS)
def test_partition_less(array):
    """Test partition for lower segment.

    Test values lower than the index are all lower than the
    index returned by partition."""
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
    """Test partition for greater segment.

    Test values greater than the index are all greater than the index
    returned by partition."""
    from .quicksort import partition
    array = array[:]
    index = partition(array, 0, len(array))
    try:
        lo = min(array[index + 1:])
    except ValueError:
        lo = float('+inf')
    assert lo >= array[index]


@pytest.mark.parametrize('array', TEST_LISTS)
def test_quicksort(array):
    from .quicksort import quicksort
    array = array[:]
    print(array)
    quicksort(array)
    assert array == sorted(array)
