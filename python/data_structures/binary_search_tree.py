from data_structures.binary_tree import BinaryTree, Node
"""
"""


class BinarySearchTree(BinaryTree):

    def add(self, value):
        if value is None:
            return

        if self.root is None:
            self.root = Node(value)
            return

        def traverse(root, new_node):

            if new_node.value < root.value:

                if root.left is not None:
                    traverse(root.left, new_node)
                else:
                    root.left = new_node
            else:

                if root.right is not None:
                    traverse(root.right, new_node)
                else:
                    root.right = new_node
        traverse(self.root, Node(value))

    def contains(self, val):

        def search(root, value):

            if root is None:
                return False

            elif root.value == value:
                return True

            elif root.value < value:
                return search(root.right, value)

            else:
                return search(root.left, value)
        return search(self.root, val)


