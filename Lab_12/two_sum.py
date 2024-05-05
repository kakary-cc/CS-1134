from ChainingHashTableMap import *


def two_sum(lst, target):
    seen = ChainingHashTableMap()
    for i in lst:
        try:
            if seen[target-i]:
                return (i, target-i)
        except KeyError:
            seen[i] = 1
    return None, None

# Test Cases
lst1 = [-2, 11, 15, 21, 20, 7]
print(two_sum(lst1, 22))

lst2 = [-2, 11, 15, 21, 20, 17]
print(two_sum(lst2, 22))
