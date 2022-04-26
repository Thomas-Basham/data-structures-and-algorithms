# Challenge 06 Summary
Write the following methods for the Linked List class:

    append
        arguments: new value
        adds a new node with the given value to the end of the list
    insert before
        arguments: value, new value
        adds a new node with the given new value immediately before the first node that has the value specified
    insert after
        arguments: value, new value
        adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

## Approach & efficiency
### Append:
For this method I used a conditional statement to instantiate a new node if there are no nodes in the Linked List. If the linked list is populated, a while loop runs until the end of the list and then points to the new Node with the input value
### Insert Before:
For this method I used a while loop that runs while until next is none through the 'pointers' to the next node. If the value of next reaches the target value, the new node is instantiated and the target value pointer is now the head pointer. If the head is the target value, the new node pointer is moved to the head
### Insert After:
For this method I used a near identical approach as the insert before method, but this time running while a node exists. If the head reaches the target value, a new node is instantiated with the previous node pointing to the new node
## Solution
[Challenge 06 Code](/python/data_structures/linked_list.py)

 - [X] Top-level README “Table of Contents” is updated
 - [X] README for this challenge is complete
   - [x] Summary, Description, Approach & Efficiency, Solution
   - [ ] Picture of whiteboard
   - [X] Link to code
 - [X] Feature tasks for this challenge are completed
 - [X] Unit tests written and passing
   - [X] “Happy Path” - Expected outcome
   - [X] Expected failure
   - [X] Edge Case (if applicable/obvious)
