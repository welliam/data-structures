# -*- coding: utf-8 -*-

"""Implement sorting algorithms."""

import sys
import random
import timeit


def build_lists():
    """Build lists for demo."""
    list1 = [x for x in range(0, 10000)]
    list2 = [x for x in range(10000, 0, -1)]
    list3 = [random.randint(0, 10000) for x in range(0, 10000)]
    list4 = [random.randint(0, 10000) for x in range(0, 10000)]
    list5 = [random.randint(0, 10000) for x in range(0, 10000)]
    list6 = [random.randint(0, 10000) for x in range(0, 10000)]
    list7 = [random.randint(0, 10000) for x in range(0, 10000)]
    return [list1, list2, list3, list4, list5, list6, list7]


def insertion_sort(list_in):
    """Python implementation of Jon Bentley's insertion sort algorithm.

    List_in is a list of numbers.
    Reference: Bentley, Jon (2000). Programming Pearls.
    ACM Press/Addison–Wesley.
    """
    for inc in range(1, len(list_in)):
        curr_value = list_in[inc]
        tmp_inc = inc
        while list_in[tmp_inc - 1] > curr_value and tmp_inc >= 1:
            list_in[tmp_inc] = list_in[tmp_inc - 1]
            tmp_inc -= 1
        list_in[tmp_inc] = curr_value

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: python sorting.py')
        sys.exit(1)

    print('Let\'s sort some lists (10000 elements, 100 times each)...')
    x = build_lists()

    t = timeit.timeit(lambda: insertion_sort(x[0]), number=100)
    print('Best case: ', t)

    t = timeit.timeit(lambda: insertion_sort(x[1]), number=100)
    print('Worst case: ', t)

    print('5 random cases:')
    for i in range(2, len(x)):
        t = timeit.timeit(lambda: insertion_sort(x[i]), number=100)
        print('case:', t)

    print('program terminated.')
    sys.exit(0)
