# data-structures
Data structure implementations for Code Fellows Python 401.

## Singly linked list
The singly linked list is appropriate when you only need traversal in
one direction. It takes less memory than the doubly linked list, and
is O(1) for insertion and removal at the front of the list.

## Stack
The stack is used for sorting algorithms, language implementations
(call stack), and a variety of other algorithms.

## Doubly linked list

The doubly linked list takes more memory than the singly linked list,
as it has to contain references in both directions. However, it allows
for insert and removal at both the front and end in O(1) time. The
singly linked list is more appropriate when the functionality of the
doubly linked list is not needed; for example, when storing an unknown
number of values on the fly, both would work but the doubly linked
list would only be appropriate if those values need to be traversed in
either direction. For example, on a website with pages, the node for
the current page would be held in memory, and when moving to the next
or previous page those fields of the doubly linked list would be
needed.

## Queue

The queue is used when a first in, first out data structure is
needed. This is useful for a variety of algorithms; for example,
the shunting yard algorithm requires a queue for its output.

## Deque

The deque is like a queue but allows for operations on either side of
the queue. The deque supports append, pop, and peek (which together
act like a stack), and appendleft, popleft, and peekleft (which
together also act like a stack, operating on the other side of the
queue). Additionally, it supports a size operation. The deque is used
in algorithms for job scheduling.

## Binary Heap

The binary heap is a tree that always pops the smallest or largest value. We chose to implement a min heap, so ours will return the smallest. When a new value is pushed on, it will check to make sure that the new child is greater than its parents, and if not swap the two, and repeat this until it finds a parent that is less than the child. It is useful for a priority queue, ensuring you will always get the smallest number when you pop off the heap.