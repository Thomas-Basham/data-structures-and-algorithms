
class LinkedList:
    """
    Can successfully instantiate an empty linked list
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    Can properly insert multiple nodes into the linked list
    Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist
    Can properly return a collection of all the values that exist in the linked list
    """

    def __init__(self, value='None'):
        self.head = None
        self.value = value
        self.next = next

    def insert(self, value):

        new_node = Node(value)
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

        current = self.head
        nodes = []
        while current:
            nodes.append(current.value)
            current = current.next
        while nodes:
            return ' -> '.join('{ ' + x + ' }' for x in nodes) + " -> NULL"
        return "NULL"


class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class TargetError:
    pass


linked = LinkedList()
linked.insert("apple")
linked.insert("pear")
linked.insert("banana")
linked.insert("cucumber")
linked.insert("orange")
print(linked)
