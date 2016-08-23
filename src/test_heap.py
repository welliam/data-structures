import pytest
from binary_heap import BinaryHeap

ITERABLES = [
    "hello",
    [1, 2, 3, 4, 5],
    range(10)
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
