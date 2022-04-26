
"""
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
"""


class LinkedList:

    def __init__(self, value='None'):
        self.head = None
        self.value = value
        self.next = next

    def includes(self, value):
        node = self.head

        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def insert(self, value):
        new_node = Node(value)
        node = self.head

        new_node.next = node
        self.head = new_node

    def insert_before(self, target_value, value):
        new_node = Node(value)
        node = self.head

        if node is None:
            raise TargetError('There are no Nodes to insert before')
        if not self.includes(target_value):
            raise TargetError(f'{{ {target_value} }} does not exist')
        else:
            while node.next:
                if node.next.value == target_value:
                    new_node.next = node.next
                    node.next = new_node
                    break
            if node.value == target_value:
                new_node.next = node
                self.head = new_node

    def insert_after(self, target_value, value):
        new_node = Node(value)
        node = self.head

        while node:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                break
            raise TargetError(f'{target_value} is missing')
        if node is None:
            raise TargetError('There are no nodes')

    def append(self, value):
        new_node = Node(value)
        node = self.head

        while node.next:
            node = node.next
        if node is None:
            self.head = new_node
            return
        node.next = new_node

    def __str__(self):
        node = self.head
        nodes = []

        while node:
            nodes.append(node.value)
            node = node.next
        while nodes:
            return ' -> '.join('{ ' + node + ' }' for node in nodes) + ' -> NULL'
        return "NULL"


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class TargetError(Exception):
    pass


linked = LinkedList()
linked.insert("head")
linked.append("pear")
linked.append('last')
linked.append("banana")
linked.append("cucumber")
linked.append("tail")
print(linked)
