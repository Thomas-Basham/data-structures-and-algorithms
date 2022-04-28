def zip_lists(a, b):
    a_node = a.head
    b_node = b.head
    # account for empty LL in arguments
    if a.head is None:
        return b
    if b.head is None:
        return a

    while a_node and b_node:
        # store next pointers
        a_next = a_node.next
        b_next = b_node.next
        # swap
        b_node.next = a_next
        a_node.next = b_node
        # drive
        a_node = a_next
        b_node = b_next
    return a

