from ArrayQueue import *


def permutations(lst):
    q = ArrayQueue()
    q.enqueue([])
    while len(q.first()) < len(lst):
        tmp = q.dequeue()
        for i in lst:
            if i not in tmp:
                added = tmp.copy()
                added.append(i)
                q.enqueue(added)
    res = []
    while not q.is_empty():
        res.append(q.dequeue())
    return res


# permutations([1, 2, 3])
