# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None


    def push(self, val):
        self.head = Node(val, self.head)
