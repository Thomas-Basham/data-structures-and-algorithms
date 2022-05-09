from data_structures.queue import Queue


def multi_bracket_validation(string):
    d = {'(': ')', '{': '}', '[': ']'}
    q = Queue()

    if string[0] == ')' or string[0] == '}' or string[0] == ']':
        return False

    for item in string:
        if item == '(' or item == '{' or item == '[':
            q.enqueue(item)

        elif item == ')' or item == '}' or item == ']':
            value = q.dequeue()
            if d[value] != item:  # If dequeued value doesn't
                return False

        else:
            continue

    if q.is_empty():
        return True

    else:
        return False
