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
        while(i > 0 and heap[i] < heap[_parent(i)]):
            self.swap(i, _parent(i))
            i = _parent(i)

    def is_sorted(self, i):
        """Returns whether the value at heap[i] is sorted.

        i.e. in the proper position for pop"""
        heap = self.heap
        left, right = _children(i)
        if right >= len(heap):
            return True
        left_sorted = left >= len(heap) or heap[i] < heap[left] 
        right_sorted = right >= len(heap) or heap[i] < heap[right]
        return left_sorted and right_sorted

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
