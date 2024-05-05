from ArrayMinHeap import *


def min_merge_cost(lst):
    amp = ArrayMinHeap()
    for i in lst:
        amp.insert(i)
    total = 0
    prev = None
    while not amp.is_empty():
        var = amp.delete_min().priority
        total += var
        if prev:
            total += prev
        prev = var
    return total


print(min_merge_cost([10, 5, 2, 14, 3, 8]))
