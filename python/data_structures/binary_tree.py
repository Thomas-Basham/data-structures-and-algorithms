class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  """
								a
						b      c
					d  e    f  g

		Pre-order: A, B, D, E, C, F
		In-order: D, B, E, A, F, C
		Post-order: D, E, B, F, C, A

		Pre-order: root >> left >> right
		In-order: left >> root >> right
		Post-order: left >> right >> root
	"""

  def __init__(self):
    self.root = None
    self.order = []

  def pre_order(self):
    def preorder_traverse(tree, array):
      if tree is None:
        return

      else:
        array.append(tree.value)
        preorder_traverse(tree.left, array)
        preorder_traverse(tree.right, array)

    preorder_traverse(self.root, self.order)
    return self.order

  def in_order(self):
    def in_order_traverse(tree, array):
      if tree is None:
        return

      else:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)

    in_order_traverse(self.root, self.order)
    return self.order

  def post_order(self):
    def post_order_traverse(tree, array):
      if tree is None:
        return

      else:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)

    post_order_traverse(self.root, self.order)
    return self.order

  def find_maximum_value(self):
    self.in_order()
    self.order.sort()
    return self.order[-1]
