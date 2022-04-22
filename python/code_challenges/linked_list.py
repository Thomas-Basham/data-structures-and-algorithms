
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        return "this is a dang string"

    def insert(self, value):
        # creating a new Node with the correct value
        self.head = Node(value, self.head)

    def includes(self, target_value):

        current = self.head

        while current:
            if current.value == target_value:
                return True

            current = current.next

        return False


class Node:
    def __int__(self, value, ):
        self.value = value
        self.head = next


class TargetError:
    pass
