
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

        if node is None:
            self.head = new_node
            return

        while node.next:
            node = node.next
        node.next = new_node

    def __str__(self):
        node = self.head
        nodes = []

        while node:
            nodes.append(node.value)
            node = node.next

        while nodes:
            return ' -> '.join('{ ' + str(node) + ' }' for node in nodes) + ' -> NULL'
        return "NULL"

    def kth_from_end(self, k):
        nodes = 0
        node = self.head
        # count the nodes
        while node:
            node = node.next
            nodes += 1

        if nodes >= k:
            current = self.head
            for i in range(nodes - (k+1)):
                current = current.next

        if nodes <= k or k < 0:
            raise TargetError('yer outta range')

        return current.value

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class TargetError(Exception):
    pass


# linked = LinkedList()
# linked.insert("head")
# linked.append("pear")
# linked.append("banana")
# linked.append("avocado")
# linked.append("cucumber")
# linked.append("tail")
# linked.insert_after("banana", "cucumber")
# print(linked)
# linked.reverse()
# print(linked)
# print(linked.kth_from_end(2))
# print(linked.kth_from_end(3))
