from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
push
    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.
pop
    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack
peek
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack
is empty
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.
    """

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError
        temp = self.top
        if self.top:
            self.top = self.top.next
        temp.next = None
        self.size -= 1
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError
        return self.top.value
