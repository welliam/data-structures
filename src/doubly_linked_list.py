from linked_list import LinkedList


class Node(object):
    """Node used internally by DoublyLinkedList to chain values."""

    def __init__(self, previous_node, value, next_node):
        self.previous_node = previous_node
        self.value = value
        self.next_node = next_node


class DoublyLinkedList(LinkedList):
    def __init__(self, iterable=None):
        super(DoublyLinkedList, self).__init__(iterable)
        self.tail = None

    def push(self, value):
        self.count += 1
        self.head = Node(None, value, self.head)
        if self.tail is None:
            self.tail = self.head

    def append(self, value):
        self.count += 1
        self.tail = Node(self.tail, value, None)
        if self.head is None:
            self.head = self.tail

    def pop(self):
        if not self.head:
            raise IndexError('Doubly linked list is empty.')
        self.count -= 1
        value = self.head.value
        if self.tail == self.head:
            self.tail = None
        self.head = self.head.next_node
        return value
