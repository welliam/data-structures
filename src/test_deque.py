import pytest
from deque import Deque

NONEMPTY_ITERABLES = [
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7],
    "hello",
    (1, 2, 3, 4, 5)
]


ITERABLES = [
    [],
    [1],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7],
    "",
    "hello",
    (1, 2, 3, 4, 5)
]

NONITERABLES = [
    1, None, True, False, 1.5, lambda x: x, type, Deque
] 


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_init(iterable):
    assert Deque(iterable).peek() == iterable[0]


@pytest.mark.parametrize('iterable', ITERABLES)
def test_size(iterable):
    assert Deque(iterable).size() == len(iterable)


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_append_1(emptydeque, iterable):
    for item in iterable:
        emptydeque.append(item)
    assert emptydeque.peek() == iterable[0]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_append_2(emptydeque, iterable):
    for item in iterable:
        emptydeque.append(item)
    emptydeque.pop()
    assert emptydeque.peek() == iterable[1]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_appendleft_1(emptydeque, iterable):
    for item in iterable:
        emptydeque.appendleft(item)
    assert emptydeque.peekleft() == iterable[0]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_appendleft_2(emptydeque, iterable):
    for item in iterable:
        emptydeque.append(item)
    emptydeque.popleft()
    assert emptydeque.peekleft() == iterable[1]


def test_operations_1(emptydeque):
    emptydeque.append(1)
    emptydeque.appendleft(0)
    assert emptydeque.pop() == 1


def test_operations_2(emptydeque):
    emptydeque.append(1)
    emptydeque.appendleft(0)
    assert emptydeque.popleft() == 0


def test_empty_pop(emptydeque):
    with pytest.raises(IndexError):
        emptydeque.pop()


def test_empty_popleft(emptydeque):
    with pytest.raises(IndexError):
        emptydeque.popleft()


@pytest.mark.parametrize('noniterable', NONITERABLES)
def test_init_noniterable(noniterable):
    with pytest.raises(TypeError):
        Deque(noniterable)
