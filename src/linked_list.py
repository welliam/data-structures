# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0


    def push(self, val):
        self.head = Node(val, self.head)
        self.count += 1


    def pop(self):
        if not self.head:
            raise IndexError('Linked list is empty.')
        self.count -= 1
        popped = self.head.value
        self.head = self.head.next_node
        return popped


    def size(self):
        return self.count
