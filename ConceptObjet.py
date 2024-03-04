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



if __name__ == '__main__':
    myStack = MyStack(10)
    myStack.add_to_stack('By')
    myStack.add_to_stack('hello')
    myStack.add_to_stack('Slt')
    myStack.add_to_stack('Slt')
    myStack.add_to_stack('Slt')
    myStack.add_to_stack('Slt')
    myStack.add_to_stack('Slt')
    print(myStack.is_full())  # True
    print(myStack.is_full())  # True
    print(myStack.is_full())  # False
    myStack.add_to_stack('hi')
    print(myStack.is_full())  # True
    myStack.add_to_stack('hi')
    print(myStack.is_full())  # True
    try:
        myStack.add_to_stack('hello')  # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)
    print(myStack.pop_from_stack())  # hello
    print(myStack.is_empty())  # False
    print(myStack.pop_from_stack())  # hello
    print(myStack.is_empty())  # False
    print(myStack.pop_from_stack())  # hello
    print(myStack.is_empty())  # True
    try:
        print(myStack.pop_from_stack())  # MyEmptyStackException
    except MyEmptyStackException as e:
        print(e)
#   C o n c e p t O b j e t . p y  
 