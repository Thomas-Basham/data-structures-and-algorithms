# Challenge Summary

    Write a function called breadth first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process

<img alt='White Board' src="Tree Breadth First.png">

## Approach & Efficiency

Import Queue class and create empty list
Enqueue the tree to the list
Dequeue the list one node at a time, appending the dequed values to the list
return the list

The efficiency of this operation is **O(n)**,
since we are adding each value of the tree to a list.

## [Solution](/code_challenges/tree_breadth_first.py)


 - [X] Top-level README “Table of Contents” is updated
 - [x] README for this challenge is complete
   - [x] Summary, Description, Approach & Efficiency, Solution
   - [x] Picture of whiteboard
   - [x] Link to code
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
   - [x] “Happy Path” - Expected outcome
   - [x] Expected failure
   - [x] Edge Case (if applicable/obvious)
