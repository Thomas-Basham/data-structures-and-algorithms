
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, value=''):
        self.head = None
        self.value = value

    def insert(self, value):
        # creating a new Node with the correct value
        self.head = Node(value)

    def includes(self, target_value):

        current = self.head

        while current:
            if current.value == target_value:
                return True
            current = current.next

        return False

    def __str__(self):
        return "this is a dang string"


class Node(LinkedList):
    def __int__(self, value, ):
        self.value = value
        self.head = next


class TargetError:
    pass
