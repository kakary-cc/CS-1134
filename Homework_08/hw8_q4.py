import random
from UnsortedArrayMap import UnsortedArrayMap
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
        self.dll = DoublyLinkedList()
        for i in range(N):
            self.table[i] = UnsortedArrayMap()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        return curr_bucket[key][0]

    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        try:
            curr_bucket[key][0] = value
        except KeyError:
            curr_bucket[key] = [value, None]
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
            curr_bucket[key][1] = self.dll.add_last(key)
        if (self.n > len(self.table)):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        dll_addr = curr_bucket[key][1]
        del curr_bucket[key]
        self.n -= 1
        self.dll.delete_node(dll_addr)
        if (self.n < len(self.table) // 4):
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for key in self.dll:
            yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def main():
    ht = ChainingHashTableMap()
    ht['Alpha'] = 'a'
    ht['Bravo'] = 'b'
    ht['Charlie'] = 'c'
    for i in ht:
        print(i)
    del ht['Bravo']
    for i in ht:
        print(i)
