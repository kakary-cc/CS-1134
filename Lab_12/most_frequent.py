from ChainingHashTableMap import *


def most_frequent(lst):
    ht = ChainingHashTableMap()
    mf = (None, 0)
    for i in lst:
        try:
            ht[i] += 1
        except KeyError:
            ht[i] = 1
        if ht[i] > mf[1]:
            mf = (i, ht[i])
    return mf[0]


# Test Cases
lst1 = [5, 9, 2, 9, 0, 5, 9, 7]
print(most_frequent(lst1))

lst2 = [5, 2, 2, 9, 0, 5, 9, 7, 2]
print(most_frequent(lst2))

# Worst-Case Space Complexity
#   O(n)
#
#   O(1) if a string of lower-case and upper-case letters given
#   since the number of letters is finite