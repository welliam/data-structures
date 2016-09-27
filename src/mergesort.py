"""Python implementation of merge sorting."""

import sys
import random
import timeit


def merge_compare(t, start, middle, end):
    """Do the first step of a merge.

    i.e., compare values starting at start and middle until either
    reaches middle or end, respectively. The smaller value gets pushed
    onto the result. Return the index of the remaining values and the
    sorted result.
    """
    result = []
    left_i = start
    right_i = middle
    while left_i < middle and right_i < end:
        inc_left = False
        if t[left_i] <= t[right_i]:
            result.append(t[left_i])
            inc_left = True
        if t[left_i] >= t[right_i]:
            result.append(t[right_i])
            right_i += 1
        if inc_left:
            left_i += 1
    return left_i if left_i < middle else right_i, result


def merge(t, start, middle, end):
    """Merge parts of t at start and middle."""
    i, result = merge_compare(t, start, middle, end)
    while i < middle:
        result.append(t[i])
        i += 1
    for value in result:
        t[start] = value
        start += 1


def run_merge(t, step):
    """Run an iteration of mergesort."""
    start = 0
    while start + step < len(t):
        merge(t, start, start + step, min(len(t), start + step * 2))
        start += step * 2


def mergesort(t):
    """Sort t in place."""
    step = 1
    while step < len(t):
        run_merge(t, step)
        step *= 2


def anti_merge(arr, left, right):
    i = j = 0
    while i < len(left):
        arr[i] = left[i]
        i += 1
    while j < len(right):
        arr[i] = right[j]
        i += 1
        j += 1


def separate(arr):
    if len(arr) <= 1:
        return
    if len(arr) == 2:
        arr[0], arr[1] = arr[1], arr[0]
        return

    left = []
    right = []
    add_left = True
    for x in arr:
        (left if add_left else right).append(x)
        add_left = not add_left

    separate(left)
    separate(right)
    anti_merge(arr, left, right)


def build_lists():
    """Build lists for demo."""
    list1 = [x for x in range(0, 10000)]
    list2 = ([x for x in range(10000)])
    separate(list2)
    list3 = [random.randint(0, 10000) for x in range(0, 10000)]
    list4 = [random.randint(0, 10000) for x in range(0, 10000)]
    list5 = [random.randint(0, 10000) for x in range(0, 10000)]
    list6 = [random.randint(0, 10000) for x in range(0, 10000)]
    list7 = [random.randint(0, 10000) for x in range(0, 10000)]
    return [list1, list2, list3, list4, list5, list6, list7]


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: python mergesort.py')
        sys.exit(1)

    print('Let\'s sort some lists (10000 elements, 100 times each)...')
    x = build_lists()

    t = timeit.timeit(lambda: mergesort(x[0][:]), number=100)
    print('Best case: ', t)

    t = timeit.timeit(lambda: mergesort(x[1][:]), number=100)
    print('Worst case: ', t)

    print('5 random cases:')
    for i in range(2, len(x)):
        t = timeit.timeit(lambda: mergesort(x[i][:]), number=100)
        print('case:', t)

    print('program terminated.')
    sys.exit(0)
