from data_structures.queue import Queue
from data_structures.stack import Stack


open_list = ["[","{","("]
close_list = ["]","}",")"]


def multi_bracket_validation(lst):
    d = {'(': ')', '{': '}', '[': ']'}
    Stk = Stack()
    q = Queue()
    for item in lst:
        if item == '(' or item == '{' or item == '[':
            q.enqueue(item)
        elif item == ')' or item == '}' or item == ']':
            value = q.dequeue()
            if d[value] != item:
                return False
        else:
            continue
    if Stk.is_empty():
        return True
    else:
        return False
