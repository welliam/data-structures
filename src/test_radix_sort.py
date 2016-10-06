import pytest


RADIX_SORT_LISTS = [
    [],
    [0],
    [1],
    [1, 2],
    [2, 1],
    range(100),
    range(100, 0, -1),
    [213, 123, 64, 666, 456, 345, 38, 67, 8, 679, 58795, 89, 8, 9],
    'lkfsdjlk',
    ['a', 'ab', 'ba', 'b'],
    ['askdhjasd',
     'asldkjasldkjasdlkjaslkdjasldb',
     'lskdjasldkjasdljkasdlkjasldkjasdlkjasdlkjasldkjaslkdja',
     'b']
]

STRS = ['', 'asd', 'asdfhkjasdfhasdf']
PADDINGS = [16, 123, 50]  # all of these must be >= than len(max(STRS))


@pytest.mark.parametrize('lst', RADIX_SORT_LISTS)
def test_radix_sort(lst):
    """Test radix sort sorts input."""
    from .radix_sort import radix_sort
    assert radix_sort(lst) == sorted(lst)


@pytest.mark.parametrize('s', STRS)
@pytest.mark.parametrize('pad', PADDINGS)
def test_string_encoding_1(s, pad):
    """Test radix sort sorts input."""
    from .radix_sort import str_to_int, int_to_str
    assert s == int_to_str(str_to_int(s, pad))


@pytest.mark.parametrize('s', STRS)
@pytest.mark.parametrize('pad', PADDINGS)
def test_string_encoding_2(s, pad):
    """Test radix sort sorts input."""
    from .radix_sort import str_to_int, int_to_str
    assert s == int_to_str(str_to_int(int_to_str(str_to_int(s, pad)), pad))
