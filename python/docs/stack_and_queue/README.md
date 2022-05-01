# Stacks and Queues
## [Code for Stack](python/data_structures/stack.py)
## [Code for Queue](python/data_structures/queue.py)
## Challenge
Using a Linked List as the underlying data storage mechanism,
implement both a Stack and a Queue
You have access to the Node class and all the properties on the Linked List class.

- [x] Can successfully push onto a stack
- [x] Can successfully push multiple values onto a stack
- [x] Can successfully pop off the stack
- [x] Can successfully empty a stack after multiple pops
- [x] Can successfully peek the next item on the stack
- [x] Can successfully instantiate an empty stack
- [x] Calling pop or peek on empty stack raises exception
- [x] Can successfully enqueue into a queue
- [x] Can successfully enqueue multiple values into a queue
- [x] Can successfully dequeue out of a queue the expected value
- [x] Can successfully peek into a queue, seeing the expected value
- [x] Can successfully empty a queue after multiple dequeues
- [x] Can successfully instantiate an empty queue
- [x] Calling dequeue or peek on empty queue raises exception


## Approach & Efficiency
All of these methods have an efficiency of O(1)

## API
Stack

    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
        This object should be aware of a default empty value assigned to top when the stack is created.
        The class should contain the following methods:
        push
            Arguments: value
            adds a new node with that value to the top of the stack with an O(1) Time performance.
        pop
            Arguments: none
            Returns: the value from node from the top of the stack
            Removes the node from the top of the stack
            Should raise exception when called on empty stack
        peek
            Arguments: none
            Returns: Value of the node located at the top of the stack
            Should raise exception when called on empty stack
        is empty
            Arguments: none
            Returns: Boolean indicating whether or not the stack is empty.

Queue

    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
        This object should be aware of a default empty value assigned to front when the queue is created.
        The class should contain the following methods:
        enqueue
            Arguments: value
            adds a new node with that value to the back of the queue with an O(1) Time performance.
        dequeue
            Arguments: none
            Returns: the value from node from the front of the queue
            Removes the node from the front of the queue
            Should raise exception when called on empty queue
        peek
            Arguments: none
            Returns: Value of the node located at the front of the queue
            Should raise exception when called on empty stack
        is empty
            Arguments: none
            Returns: Boolean indicating whether or not the queue is empty

