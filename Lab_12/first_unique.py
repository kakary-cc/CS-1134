from ChainingHashTableMap import *


def first_unique(lst):
    ht = ChainingHashTableMap()
    for i in lst:
        try:
            ht[i] += 1
        except KeyError:
            ht[i] = 1
    for i in lst:
        try:
            if ht[i] == 1:
                return i
        except KeyError:
            pass
    return None


# Test Cases
lst1 = [5, 9, 2, 9, 0, 5, 9, 7]
print(first_unique(lst1))

lst2 = [5, 2, 2, 9, 0, 5, 9, 7, 2]
print(first_unique(lst2))

# Worst-Case Space Complexity
#   O(n)
#
#   O(1) if a string of lower-case and upper-case letters given
#   since the number of letters is finite
