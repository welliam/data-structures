# data-structures
[![Build Status](https://travis-ci.org/welliam/data-structures.svg?branch=bst-traversal)](https://travis-ci.org/welliam/data-structures)

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

The binary heap is a tree that always pops the smallest or largest
value. We chose to implement a min heap, so ours will return the
smallest. When a new value is pushed on, it will check to make sure
that the new child is greater than its parents, and if not swap the
two, and repeat this until it finds a parent that is less than the
child. It is useful for a priority queue, ensuring you will always get
the smallest number when you pop off the heap.

## Directed Graph

The directed graph is a data structure that consists of nodes and
edges which connect them in zero, one, or both ways. The graph can be
queried for whether a particular node is a neighbor of another, and
nodes and edges can be deleted; if a node is deleted, all of the edges
involving that node are deleted as well. The graph can be used as a
model for networking applications.

Edges in the graph are weighted, although nothing takes advantage of
or uses the weights yet.

I read about graph implementations [on
Wikipedia](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)).

### Graph Traversal

Graph traversal is traversing the graph in a certain way. The
adjacency_list.py file implements a graph with both depth-first and
breadth-first traversal. Graph traversal is useful for a wide range of
applications, and is commonly used wherever graphs are used (for
modeling networks, as well as a wide range of algorithms in general).

I read about breadth first searching [on
Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search).

## Binary Search Tree
          
The binary search tree (BST) is a data structure that consists of
nodes, which may have up to two children (left and right). For each
node in the BST, the node's left child must always be less than the
node's value, and the node's right child must always be greater than
the node's value. This allows for quick searching of inserted
values. The binary search tree is used in sorting algorithms and other
situations where storing values with quick searching is needed.

Our BST has two methods for insertion-- insert and
asymmetrical_insert. after inserting a value, insert rebalances the
tree like it's an AVL tree. asymmetrical_insert does no rebalancing;
this can be useful when one requires specific results from the
traversal methods.

### Binary Search Tree Traversal

The BST implementation has four types of traversal methods:
breadth_first, and three depth first traversal methods:
- pre_order, which orders the top node's value before iterating first upon
  the left and then upon the right branches,
- post_order, which orders the left node's values before the right
  node's values before finally the top node's value,
- in_order, which returns the binary search tree's values sorted

### Binary Search Tree Deletion

We implement binary search tree removal. When deleting a node with
zero or one branch, the algorithm simply replaces the branch
containing the deleted node with either None or the single
branch. Otherwise, the algorithm find the maximum node that is less
than the node to be deleted and continually move that branch downwards
to the left. Finally, the algorithm replace the node to be deleted
with the max node, and remove the reference to that node.


## Mergesort

Our merge algorithm implements mergesort, a divide and conquer sorting
algorithm. It uses a _merge_ algorithm that combines two sorted chunks
of an array. _merge_ is called on first every adjacent value, then on
those sorted chunks, etc. until the list is sorted. This
implementation is purely iterative, so arrays of any size will not
cause a stack overflow. The space usage is O(n), as an auxiliary array
is required to build sorted portions. The program clearly reveals the
time usage, O(nlog(n)); an outer loop, mergesort, iterates with a step
that is multiplied by two every iteration (the O(log(n)) factor) and
an inner loop iterates a constant number of times for each value in
the array it's sorting (the O(n) factor).

[This Stack Overflow
answer](http://stackoverflow.com/questions/2673651/inheritance-from-str-or-int)
was referenced for the implementation of TaggedInt, a class used in
the tests for stability.
