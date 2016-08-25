# -*- coding: utf-8 -*-

"""Test heap functionality."""

import pytest
from binary_heap import BinaryHeap
from random import sample

ITERABLES = [
    "hello",
    [5, 1, 2, 7, 3, 4, -592034, 5],
    range(10),
    range(10, 0, -1),
    sample(list(range(20)), 20),
    sample(list(range(300)), 300),
    sample(list(range(1000)), 1000)
]

NONITERABLES = [lambda x: x, 1, True]


def test_basic_pushpop(emptyheap):
    """Test basic push and pop."""
    emptyheap.push(0)
    assert emptyheap.pop() == 0

    
def test_heap_1(emptyheap):
    emptyheap.push(1)
    emptyheap.push(2)
    emptyheap.push(3)
    assert emptyheap.pop() == 1


def test_heap_2(emptyheap):
    emptyheap.push(1)
    emptyheap.push(2)
    emptyheap.push(3)
    emptyheap.pop()
    assert emptyheap.pop() == 2


def test_heap_3(emptyheap):
    emptyheap.push(1)
    emptyheap.push(2)
    emptyheap.push(3)
    print('vvv')
    print(emptyheap)
    emptyheap.pop()
    print(emptyheap)
    emptyheap.pop()
    print(emptyheap)
    print('^^^')
    assert emptyheap.pop() == 3


@pytest.mark.parametrize('iterable', ITERABLES)
def test_init(iterable):
    """Test initialization method."""
    h = BinaryHeap(iterable)
    assert h.pop() == min(iterable)


@pytest.mark.parametrize('noniterable', NONITERABLES)
def test_init_error(noniterable):
    """Test initialization method throws TypeError

    When passed a non-iterable.
    """
    with pytest.raises(TypeError):
        BinaryHeap(noniterable)


@pytest.mark.parametrize('iterable', ITERABLES)
def test_max_init(iterable):
    """Test initialization method."""
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    assert h.pop() == max(iterable)


@pytest.mark.parametrize('iterable', ITERABLES)
def test_minimum(iterable):
    """Test that sequential pops return larger values."""
    h = BinaryHeap(iterable)
    minimum = h.pop()
    assert minimum < h.pop()


def test_empty_pop(emptyheap):
    """Test that pop on an empty heap raises an IndexError."""
    with pytest.raises(IndexError):
        emptyheap.pop()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_binheap(iterable):
    """Test that pop values from max heap are sorted."""
    h = BinaryHeap(iterable)
    results = []
    try:
        for _ in iterable:
            results.append(h.pop())
    except IndexError:
        assert sorted(results) == results


@pytest.mark.parametrize('iterable', ITERABLES)
def test_binheap_2(iterable):
    """Test that pop values from heap are sorted."""
    h = BinaryHeap(iterable)
    results = []
    for _ in range(len(iterable)//2):
        h.pop()
    for x in iterable:
        h.push(x)
    for _ in iterable:
        results.append(h.pop())
    assert sorted(results) == results


@pytest.mark.parametrize('iterable', ITERABLES)
def test_max_binheap(iterable):
    """Test that pop values from max heap are sorted."""
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    results = []
    try:
        for _ in iterable:
            results.append(h.pop())
    except IndexError:
        assert sorted(results, reverse=True) == results


@pytest.mark.parametrize('iterable', ITERABLES)
def test_valid_binheap(iterable):
    """Test that h.valid() returns true after some pops."""
    h = BinaryHeap(iterable)
    for i in range(len(iterable)//2):
        h.pop()
    assert h.valid()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_valid_max_binheap(iterable):
    """Test that h.valid() returns true after some pops.

    (When compare is provided.)
    """
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    for i in range(len(iterable)//2):
        h.pop()
    assert h.valid()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_heap_peek(iterable):
    h = BinaryHeap(iterable)
    assert h.peek() == min(iterable)


@pytest.mark.parametrize('iterable', ITERABLES)
def test_max_heap_peek(iterable):
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    assert h.peek() == max(iterable)


@pytest.mark.parametrize('iterable', ITERABLES)
def test_peek_pop_equivalent_1(iterable):
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    assert h.peek() == h.pop()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_peek_pop_equivalent_2(iterable):
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    for _ in range(len(iterable) // 2):
        h.pop()
    assert h.peek() == h.pop()


def test_peek_failure(emptyheap):
    with pytest.raises(IndexError):
        emptyheap.peek()
