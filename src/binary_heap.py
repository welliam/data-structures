def _children(i):
    return 2*i+1, 2*i+2


def _parent(i):
    return (i-1) // 2


class BinaryHeap(object):
    def __init__(self, iterable=None):
        self.heap = []
        if iterable:
            for value in iterable:
                self.push(value)

    def __repr__(self):
        return str(self.heap)

    def swap(self, i1, i2):
        heap = self.heap
        heap[i1], heap[i2] = heap[i2], heap[i1]

    def push(self, x):
        heap = self.heap
        heap.append(x)
        i = len(heap) - 1
        while i > 0:
            parent = _parent(i)
            if heap[i] > heap[parent]:
                return
            self.swap(i, parent)
            i = parent

    def branch_sorted(self, i, branch):
        """Return whether branch of index i is sorted.

        i.e. in the proper position for pop"""
        return branch >= len(self.heap) or self.heap[i] < self.heap[branch]

    def is_sorted(self, i):
        """Return whether the value at heap[i] is sorted.

        i.e. in the proper position for pop"""
        heap = self.heap
        left, right = _children(i)
        if right >= len(heap):
            return True
        return self.branch_sorted(i, left) and self.branch_sorted(i, right)

    def pop(self):
        heap = self.heap
        value = heap[0]
        try:
            heap[0] = heap.pop()
        except IndexError:
            return value
        i = 0
        while(i < (len(heap)) and not self.is_sorted(i)):
            left, right = _children(i)
            to_swap = left if heap[left] < heap[right] else right
            self.swap(i, to_swap)
            i = to_swap
        return value
