import random
from DoublyLinkedList import *
import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ChainingHashTableMap:

    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def add(self, key):
        curr_bucket = self.table[self.h(key)]
        for i in curr_bucket:
            if i == key:
                return
        curr_bucket.add_last(key)
        self.n += 1
        if self.n > len(self.table):
            self.rehash(2 * len(self.table))

    def remove(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        curr_bucket: DoublyLinkedList
        for i in curr_bucket:
            if i == key:
                curr_bucket.delete_node(i)
        self.n -= 1
        if self.n < len(self.table) // 4:
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            val = self.h[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key

    def rehash(self, new_size):
        old = [key for key in self]
        self.__init__(new_size)
        for key in old:
            self.add(key)


def print_hash_table(hset):
    print('{ ', end='')
    for i in hset:
        print(i, end=' ')
    print('}')


set1 = ChainingHashTableMap()
for i in range(9):
    set1.add(i)
print_hash_table(set1)

set2 = ChainingHashTableMap()
for _ in range(9):
    set2.add(2)
print_hash_table(set2)
