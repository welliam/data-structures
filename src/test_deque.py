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
    1, True, False, 1.5, lambda x: x, type, Deque
]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_init(iterable):
    """Test initialization method."""
    assert Deque(iterable).peek() == iterable[0]


@pytest.mark.parametrize('iterable', ITERABLES)
def test_size(iterable):
    """Test size method."""
    assert Deque(iterable).size() == len(iterable)


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_append_1(emptydeque, iterable):
    """Test append method."""
    for item in iterable:
        emptydeque.append(item)
    assert emptydeque.peek() == iterable[-1]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_append_2(emptydeque, iterable):
    """Test append method."""
    for item in iterable:
        emptydeque.append(item)
    emptydeque.pop()
    assert emptydeque.peek() == iterable[-2]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_appendleft_1(emptydeque, iterable):
    """Test appendleft method."""
    for item in iterable:
        emptydeque.appendleft(item)
    assert emptydeque.peekleft() == iterable[-1]


@pytest.mark.parametrize('iterable', NONEMPTY_ITERABLES)
def test_appendleft_2(emptydeque, iterable):
    """Test appendleft method."""
    for item in iterable:
        emptydeque.appendleft(item)
    emptydeque.popleft()
    assert emptydeque.peekleft() == iterable[-2]


def test_operations_1(emptydeque):
    """Test combination of append and appendleft."""
    emptydeque.append(1)
    emptydeque.appendleft(0)
    assert emptydeque.pop() == 1


def test_operations_2(emptydeque):
    """Test combination of append and appendleft."""
    emptydeque.append(1)
    emptydeque.appendleft(0)
    assert emptydeque.popleft() == 0


def test_empty_pop(emptydeque):
    """Test pop raises IndexError on empty deque."""
    with pytest.raises(IndexError):
        emptydeque.pop()


def test_empty_pop_2(emptydeque):
    """Test pop raises IndexError on empty deque."""
    emptydeque.append(1)
    emptydeque.pop()
    with pytest.raises(IndexError):
        emptydeque.pop()

def test_empty_popleft_1(emptydeque):
    """Test pop raises IndexError on empty deque."""
    with pytest.raises(IndexError):
        emptydeque.popleft()


def test_empty_popleft_2(emptydeque):
    """Test pop raises IndexError on empty deque."""
    emptydeque.append(1)
    emptydeque.pop()
    with pytest.raises(IndexError):
        emptydeque.popleft()


@pytest.mark.parametrize('noniterable', NONITERABLES)
def test_init_noniterable(noniterable):
    """Test pop raises TypeError on empty deque."""
    with pytest.raises(TypeError):
        Deque(noniterable)


def test_stack(emptydeque):
    """Test deque operations which treat it like a stack.

    (append and pop)."""
    emptydeque.append(1)
    emptydeque.append(2)
    assert emptydeque.pop() == 2


def test_stack_2(emptydeque):
    """Test deque operations which treat it like a stack.

    (append and pop)."""
    emptydeque.append(1)
    emptydeque.append(2)
    emptydeque.pop()
    assert emptydeque.pop() == 1


def test_stack_left(emptydeque):
    """Test deque operations which treat it like a stack.

    (appendleft and popleft)."""
    emptydeque.appendleft(1)
    emptydeque.appendleft(2)
    assert emptydeque.popleft() == 2


def test_stack_left_2(emptydeque):
    """Test deque operations which treat it like a stack.

    (appendleft and popleft)."""
    emptydeque.appendleft(1)
    emptydeque.appendleft(2)
    emptydeque.popleft()
    assert emptydeque.popleft() == 1
