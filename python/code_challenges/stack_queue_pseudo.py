from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.top = None
        self.inbox = Stack()
        self.outbox = Stack()
        self.size = 0

    def enqueue(self, value):
        Stack.push(self, value)

    def is_empty(self):
        return self.size == 0

    def dequeue(self):
        Stack.pop(self)


