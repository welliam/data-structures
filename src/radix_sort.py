from math import log10
from src.queue import Queue


def radix_sort(values):
    """Implement radix sort with a radix of 10."""
    if not values:
        return values
    buckets = [Queue() for _ in range(10)]
    for i in range(int(log10(max(values)) + 1)):
        for value in values:
            buckets[value // 10**i % 10].enqueue(value)
        values = []
        for bucket in buckets:
            while bucket.size():
                values.append(bucket.dequeue())
    return values
