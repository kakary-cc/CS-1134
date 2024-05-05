from DoublyLinkedList import *


class LinkedQueue:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, e):
        self.dll.add_last(e)

    def dequeue(self):
        return self.dll.delete_first()

    def first(self):
        return self.dll.header.next.data
