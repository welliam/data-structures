from math import log10
from src.queue import Queue


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
