# Trees
[Binary Trees](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
## Challenge
Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            pre order
            in order
            post order which returns an array of the values, ordered appropriately.
    Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree

    Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        Add
            Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
        Contains
            Argument: value
            Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

I used a list stack as a property of the BinaryTree class.
The efficiency of this method is O(n) where n is the size of the tree
since we have to add each node to a list.

## API
ALGORITHM preOrder(root)

  OUTPUT <-- root.value

  if root.left is not NULL
      preOrder(root.left)

  if root.right is not NULL
      preOrder(root.right)

ALGORITHM inOrder(root)
// INPUT <-- root node
// OUTPUT <-- in-order output of tree node's values

    if root.left is not NULL
        inOrder(root.left)

    OUTPUT <-- root.value

    if root.right is not NULL
        inOrder(root.right)

ALGORITHM postOrder(root)
// INPUT <-- root node
// OUTPUT <-- post-order output of tree node's values

    if root.left is not NULL
        postOrder(root.left)

    if root.right is not NULL
        postOrder(root.right)

    OUTPUT <-- root.value




1. [x] Can successfully instantiate an empty tree
2. [x] Can successfully instantiate a tree with a single root node
3. [x] For a Binary Search Tree, can successfully add a left child and right child properly to a node
4. [x] Can successfully return a collection from a preorder traversal
5. [x] Can successfully return a collection from an inorder traversal
6. [x] Can successfully return a collection from a postorder traversal
7. [x] Returns true/false for the contains method, given an existing or non-existing node value

