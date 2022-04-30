from linked_list import Node, LinkedList
from invalid_operation_error import InvalidOperationError
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

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        temp = Node(value)
        if self.tail is None:
            self.front = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def dequeue(self):

        if self.tail is None:
            raise InvalidOperationError
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.tail = None
        self.size -= 1

        return temp.value

    def peek(self):
      if self.front:
          return self.front.value
      else:
          raise InvalidOperationError

    def __str__(self):

        node = self.front
        nodes = []

        while node:
            nodes.append(node.value)
            node = node.next

        while nodes:
            return ' -> '.join('{ ' + str(node) + ' }' for node in nodes) + ' -> NULL'
        return "NULL"


q = Queue()
q.enqueue("front")
q.enqueue("next")
q.enqueue("last")
q.dequeue()

print(q)
