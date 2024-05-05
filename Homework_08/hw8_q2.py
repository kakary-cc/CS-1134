from ChainingHashTableMap import *


def intersection_list(lst1, lst2):
    hashtable = ChainingHashTableMap()
    intersect = []
    for i in lst1:
        hashtable[i] = 1
    for i in lst2:
        if i in hashtable:
            intersect.append(i)
        else:
            hashtable[i] = 1
    return intersect

def main():
    lst1 = [3, 9, 2, 7, 1]
    lst2 = [4, 1, 8, 2]
    print(intersection_list(lst1, lst2))
