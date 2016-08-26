from .linked_list import LinkedList


class Node(object):
    """Node used internally by DoublyLinkedList to chain values."""

    def __init__(self, previous_node, value, next_node):
        """Initialize a node."""
        self.previous_node = previous_node
        self.value = value
        self.next_node = next_node


class DoublyLinkedList(LinkedList):
    """Implement DoublyLinkedList abstract data type."""

    def __init__(self, iterable=None):
        """Initialize a linked list."""
        self.tail = None
        super(DoublyLinkedList, self).__init__(iterable)

    def push(self, value):
        """Push a value onto the front of the list."""
        self.count += 1
        self.head = Node(None, value, self.head)
        if self.tail is None:
            self.tail = self.head
        else:
            self.head.next_node.previous_node = self.head

    def append(self, value):
        """Append a value onto the end of the list."""
        self.count += 1
        self.tail = Node(self.tail, value, None)
        if self.head is None:
            self.head = self.tail
        else:
            self.tail.previous_node.next_node = self.tail

    def pop(self):
        try:
            value = self.head.value
        except AttributeError:
            raise IndexError('Doubly linked list is empty.')
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
        self.count -= 1
        return value

    def shift(self):
        try:
            value = self.tail.value
        except AttributeError:
            raise IndexError('Doubly linked list is empty.')
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
        self.count -= 1
        return value

    def remove(self, val):
        """Remove the first node with val as its value."""
        node = self.search(val)
        if not node:
            raise IndexError('Remove() called for value not in list')
        if node.previous_node is None:
            self.head = node.next_node
        else:
            node.previous_node.next_node = node.next_node
        if node.next_node is None:
            self.tail = node.previous_node
        else:
            node.next_node.previous_node = node.previous_node
        self.count -= 1
