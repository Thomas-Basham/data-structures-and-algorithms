from data_structures.binary_tree import BinaryTree

"""

Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

"""


def tree_intersection(tree_a, tree_b):
    intersected = []
    a_list = BinaryTree.in_order(tree_a)
    b_list = BinaryTree.in_order(tree_b)

    for value in a_list:
        if value in b_list:
            intersected.append(value)

    return sorted(intersected)




