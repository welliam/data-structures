import sys
import random
import timeit
from math import log10
from .queue import Queue


ASCII_RADIX = 128


def str_to_int(s, padding):
    """Convert a string to an number.

    Represents each character as a digit of a base-128 number."""
    res = 0
    for c in s:
        res *= ASCII_RADIX  # ascii
        res += ord(c)
        padding -= 1
    res *= ASCII_RADIX ** padding
    return res


def int_to_str(n):
    """Convert a number to a string.

    Represents each character as a digit of a base-128 number."""
    while n and n % 128 == 0:
        n //= 128
    res = ''
    while n:
        res = chr(n % 128) + res
        n //= 128
    return res


def radix_sort(values):
    """Implement radix sort with a radix of 10."""
    if not values:
        return values
    sorting_string = isinstance(values[0], str)
    if sorting_string:
        max_length = max(map(len, values))
        values = [str_to_int(value, max_length) for value in values]
    buckets = [Queue() for _ in range(10)]
    largest = max(values)
    for i in range(not largest or int(log10(largest) + 1)):
        for value in values:
            buckets[value // 10**i % 10].enqueue(value)
        values = []
        for bucket in buckets:
            while bucket.size():
                values.append(bucket.dequeue())
    if sorting_string:
        return [int_to_str(value) for value in values]
    return values


def build_lists():
    """Build lists for demo."""
    list1 = [x for x in range(0, 1000)]
    list2 = [x for x in range(1000, 0, -1)]
    list3 = [random.randint(0, 1000) for x in range(0, 1000)]
    list4 = [random.randint(0, 1000) for x in range(0, 1000)]
    list5 = [random.randint(0, 1000) for x in range(0, 1000)]
    list6 = [random.randint(0, 1000) for x in range(0, 1000)]
    list7 = [random.randint(0, 1000) for x in range(0, 1000)]
    return [list1, list2, list3, list4, list5, list6, list7]


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: python radix_sort.py')
        sys.exit(1)

    print('Let\'s sort some lists (1000 elements, 100 times each)...')
    x = build_lists()

    t = timeit.timeit(lambda: radix_sort(x[0]), number=100)
    print('Pre-sorted case: ', t)

    t = timeit.timeit(lambda: radix_sort(x[1]), number=100)
    print('Reversed case: ', t)

    print('5 random cases:')
    for i in range(2, len(x)):
        t = timeit.timeit(lambda: radix_sort(x[i]), number=100)
        print('case:', t)

    print('program terminated.')
    sys.exit(0)
