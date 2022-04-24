
class LinkedList:
    """
    * Can successfully instantiate an empty linked list
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    Can properly insert multiple nodes into the linked list
    Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist
    Can properly return a collection of all the values that exist in the linked list
    """

    def __init__(self, value=None):
        self.head = None
        self.value = value
        self.next = next

    def insert(self, new_value):
        # creating a new Node with the current value
        new_node = Node(new_value)

        new_node.next = self.head

        self.head = new_node

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):
        # variable for iteration
        current = self.head

        # iterating until we reach the end of the linked list
        while current is not None:
            # printing the node data
            # moving to the next node
            # current = current.next
            return f'{{ {current.value} }} -> NULL'

        return 'NULL'


class Node(LinkedList):
    def __int__(self, value):
        self.value = value
        self.next = None


class TargetError:
    pass
