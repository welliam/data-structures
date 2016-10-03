"""This is a python implementation of the quicksort method."""

import sys
import random
import timeit


def partition(array, lo, hi):
    """Parititon array in specified segment."""
    pivot = array[hi - 1]
    i = j = lo
    while j < hi:
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    return i - 1


def quicksort(array):
    """Sort array."""
    stack = [(0, len(array))]
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            p = partition(array, lo, hi)
            stack.append((p + 1, hi))
            stack.append((lo, p))


def build_lists():
    """Build lists for demo."""
    list1 = [x for x in range(0, 100, 2)] + [x for x in range(99, 1, 2)]
    list2 = [x for x in range(0, 100)]
    list3 = [random.randint(0, 100) for x in range(0, 100)]
    list4 = [random.randint(0, 100) for x in range(0, 100)]
    list5 = [random.randint(0, 100) for x in range(0, 100)]
    list6 = [random.randint(0, 100) for x in range(0, 100)]
    list7 = [random.randint(0, 100) for x in range(0, 100)]
    return [list1, list2, list3, list4, list5, list6, list7]


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: python quicksort.py')
        sys.exit(1)

    print('Let\'s sort some lists (100 elements, 100 times each)...')
    x = build_lists()

    t = timeit.timeit(lambda: quicksort(x[0]), number=100)
    print('Best case: ', t)

    t = timeit.timeit(lambda: quicksort(x[1]), number=100)
    print('Worst case: ', t)

    print('5 random cases:')
    for i in range(2, len(x)):
        t = timeit.timeit(lambda: quicksort(x[i]), number=100)
        print('case:', t)

    print('program terminated.')
    sys.exit(0)
