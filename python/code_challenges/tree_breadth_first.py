from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue
"""
ALGORITHM breadthFirst(root)
// INPUT  <-- root node
// OUTPUT <-- front node of queue to console

  Queue breadth <-- new Queue()
  breadth.enqueue(root)

  while ! breadth.is_empty()
    node front = breadth.dequeue()
    OUTPUT <-- front.value

    if front.left is not NULL
      breadth.enqueue(front.left)

    if front.right is not NULL
      breadth.enqueue(front.right)

"""


def breadth_first(tree):

    q = Queue()
    values = []

    if tree.root is None:
        return values

    q.enqueue(tree.root)

    while q.front is not None:
        front = q.dequeue()
        values.append(front.value)

        if front.left is not None:
            q.enqueue(front.left)

        if front.right is not None:
            q.enqueue(front.right)

    return values



def fizz_buzz_tree(k_ary_tree):
    breadth_first_order = breadth_first(k_ary_tree)
    result = []
    for node in breadth_first_order:
        if node % 3 == 0 and node % 5 == 0:
            result.append("fizzbuzz")

        elif node % 3 == 0:
            result.append("fizz")

        elif node % 5 == 0:
            result.append("buzz")

        else:
            result.append(str(node))
    for i in result:
        K_ary_tree().add(i)
    return K_ary_tree

