# Challenge 06 Summary
Write the following method for the Linked List class:

    kth from end
        argument: a number, k, as a parameter.
        Return the node’s value that is k places from the tail of the linked list.
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process
![whiteboard](Challenge 07 Linked List Zip.png)
<img src="Challenge 07 Linked List Zip.png">
[White Board link](https://lucid.app/lucidspark/17272d16-7c21-46b9-9243-04696b3e80e9/edit?invitationId=inv_ee300c23-27bf-468e-9daa-be7246057640)

## Approach & efficiency
For this approach I used a loop with two pointers,
switching the pointers until the list ends.
I had trouble getting two of the tests to pass.
I am pretty certain the test_a_shorter is failing because
the loop is breaking once a is pointing to none.
I think I can use a method from the Linked List class
to help solve that. Another is failing for odd reasons that
I don't know yet.
## Solution
[Challenge 07 Code](/python/code_challenges/linked_list_zip.py)

## Check List
 - [x] Top-level README “Table of Contents” is updated
 - [x] README for this challenge is complete
   - [x] Summary, Description, Approach & Efficiency, Solution
   - [x] Picture of whiteboard
   - [x] Link to code
 - [X] Feature tasks for this challenge are completed
 - [ ] Unit tests written and passing
   - [X] “Happy Path” - Expected outcome
   - [ ] Expected failure
   - [ ] Edge Case (if applicable/obvious)
