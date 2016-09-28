"""This is a python implementation of the quicksort method."""


def partition(array, lo, hi):
    pivot = array[hi - 1]
    i = j = lo
    while j < hi:
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    return i - 1


def quicksort(array):
    stack = [(0, len(array))]
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            p = partition(array, lo, hi)
            stack.append((p + 1, hi))
            stack.append((lo, p))
