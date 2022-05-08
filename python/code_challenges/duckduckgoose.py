from data_structures.queue import Queue


def duck_duck_goose(namelist, num):
    Q = Queue()

    for name in namelist:
        Q.enqueue(name)

    while Q.size > 1:
        Q.dequeue()
        for i in range(num):
            Q.enqueue(Q.dequeue())

    return Q.peek()

