class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.top = None

    def add_to_stack(self, item):
        if self.size >= self.max_size:
            raise MyOutOfSizeException("Stack is full")
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.size == 0:
            raise MyEmptyStackException("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size



 
