# -*- coding: utf-8 -*-

"""Test heap functionality."""

import pytest
from binary_heap import BinaryHeap
from random import sample, randint

ITERABLES = [
    "hello",
    [5, 1, 2, 7, 3, 4, -592034, 5],
    range(10),
    range(10, 0, -1),
    sample(list(range(10000)), 10000)
]


def test_basic_pushpop(emptyheap):
    """Test basic push and pop."""
    emptyheap.push(0)
    assert emptyheap.pop() == 0


@pytest.mark.parametrize('iterable', ITERABLES)
def test_init(iterable):
    """Test initialization method."""
    h = BinaryHeap(iterable)
    assert h.pop() == min(iterable)


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
    """Test that pop values from heap are sorted."""
    h = BinaryHeap(iterable)
    results = []
    try:
        results.append(h.pop())
    except IndexError:
        assert sorted(results) == results


@pytest.mark.parametrize('iterable', ITERABLES)
def test_max_binheap(iterable):
    """Test that pop values from max heap are sorted."""
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    results = []
    try:
        results.append(h.pop())
    except IndexError:
        assert sorted(results, reverse=True) == results


@pytest.mark.parametrize('iterable', ITERABLES)
def test_valid_binheap(iterable):
    """Test that pop values from max heap are sorted."""
    h = BinaryHeap(iterable)
    assert h.valid()


@pytest.mark.parametrize('iterable', ITERABLES)
def test_valid_max_binheap(iterable):
    """Test that pop values from max heap are sorted."""
    h = BinaryHeap(iterable, compare=lambda x, y: x > y)
    for i in range(randint(0, len(iterable))):
        h.pop()
    assert h.valid()
