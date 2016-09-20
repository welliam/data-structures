# -*- coding: utf-8 -*-

"""Implement sorting algorithms."""

import sys
import random
import timeit


def build_lists():
    """Build lists for demo."""
    list1 = [x for x in range(1000, 0)]
    list2 = [x for x in range(0, 1000)]
    list3 = [random.randint(0, 1000) for x in range(0, 1000)]
    list4 = [random.randint(0, 1000) for x in range(0, 1000)]
    list5 = [random.randint(0, 1000) for x in range(0, 1000)]
    list6 = [random.randint(0, 1000) for x in range(0, 1000)]
    list7 = [random.randint(0, 1000) for x in range(0, 1000)]
    return [list1, list2, list3, list4, list5, list6, list7]


def insertion_sort(list_in):
    """Implementation of Jon Bentley's insertion sort algorithm.

    List_in is a list of numbers.
    """
    for i in range(2, len(list_in)):
        v = list_in[i]
        j = i
        while list_in[j - 1] > v and j >= 1:
            list_in[j] = list_in[j - 1]
            j -= 1
        list_in[j] = v
    return list_in

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: python sorting.py')
        sys.exit(0)
    print('Let\'s sort some lists (1000 elements, 1000 times each)...')
    x = build_lists()
    t = timeit.timeit(lambda: insertion_sort(x[0]), number=1000)
    print('Best case: ', t)

    t = timeit.timeit(lambda: insertion_sort(x[1]), number=1000)
    print('Worst case: ', t)

    print('5 random cases:')

    for i in range(2, len(x)):
        t = timeit.timeit(lambda: insertion_sort(x[i]), number=1000)
        print('case:', t)

    print('program terminated.')
    sys.exit(1)
