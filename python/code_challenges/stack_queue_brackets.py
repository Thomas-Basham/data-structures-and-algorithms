from data_structures.queue import Queue

open_list = ["[","{","("]
close_list = ["]","}",")"]


def multi_bracket_validation(lst):
    d = {'(': ')', '{': '}', '[': ']'}
    q = Queue()

    if lst[0] == ')' or lst[0] == '}' or lst[0] == ']':
        return False

    for item in lst:
        if item == '(' or item == '{' or item == '[':
            q.enqueue(item)

        elif item == ')' or item == '}' or item == ']':
            value = q.dequeue()
            # if d[value] != item:
            #     return False
            if value not in d:
                return False

        else:
            continue

    if q.is_empty():
        return True

    else:
        return False
