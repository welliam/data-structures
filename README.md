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
