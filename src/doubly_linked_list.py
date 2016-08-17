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
        self.head = Node(None, value, self.head)
        if self.tail is None:
            self.tail = self.head
