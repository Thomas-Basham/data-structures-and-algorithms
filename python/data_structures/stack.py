from python.data_structures.linked_list import LinkedList, Node

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
        pass

    def push(self, value):
        if self.top is None:
            self.top = Node(value, None)
            return
        self.top = Node(value, self.top)

    def pop(self):

