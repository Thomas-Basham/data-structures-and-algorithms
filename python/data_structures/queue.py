from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError
class Queue:
    """
enqueue
    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.
dequeue
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue
peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack
is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty
    """
    def __init__(self):
        self.front = self.tail = None
        self.size = 0
        pass

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        temp = Node(value)
        if self.tail is None:
            self.front = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        # method body here
        pass

    def peek(self):
        # method body here
        pass

    def is_empty(self):
        # method body here
        pass
