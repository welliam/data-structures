import linked_list


class Stack():
    def __init__(self, iterable=None):
        self.linked_list = linked_list.LinkedList()
        linked_list.LinkedList.__init__(self.linked_list, iterable)

    def push(self, val):
        self.linked_list.push(val)

    def pop(self):
        return self.linked_list.pop()
