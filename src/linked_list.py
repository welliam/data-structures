# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, iterable=[]):
        self.head = None
        self.count = 0
        for value in iterable:
            self.push(value)

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

    def search(self, val):
        current_node = self.head
        while current_node:
            if current_node.value == val:
                return current_node
            current_node = current_node.next_node

    def remove(self, node):
        if self.head == node:
            self.head = self.head.next_node
        else:
            current_node = self.head
            while current_node.next_node:
                if current_node.next_node == node:
                    current_node.next_node = current_node.next_node.next_node
                    self.count -= 1
                    return
                else:
                    current_node = current_node.next_node

    def display(self):
        if self.count == 0:
            return u'()'
        else:
            current_node = self.head.next_node
            result = u'({}'.format(self.head.value)
            while current_node:
                result += u', {}'.format(current_node.value)
                current_node = current_node.next_node
            return result + u')'
