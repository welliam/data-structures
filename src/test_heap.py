import pytest
from binary_heap import BinaryHeap

ITERABLES = [
    "hello",
    [5, 1, 2, 7, 3, 4, -592034, 5],
    range(10),
    range(10, 0, -1)
]


def test_basic_pushpop(emptyheap):
    emptyheap.push(0)
    assert emptyheap.pop() == 0


@pytest.mark.parametrize('iterable', ITERABLES)
def test_init(iterable):
    h = BinaryHeap(iterable)
    assert h.pop() == min(iterable)


@pytest.mark.parametrize('iterable', ITERABLES)
def test_minimum(iterable):
    h = BinaryHeap(iterable)
    minimum = h.pop()
    assert minimum < h.pop()


def test_empty_pop(emptyheap):
    with pytest.raises(IndexError):
        emptyheap.pop()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_binheap(iterable):
    h = BinaryHeap(iterable)
    results = []
    try:
        results.append(h.pop())
    except IndexError:
        assert sorted(results) == results
