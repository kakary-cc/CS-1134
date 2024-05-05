from DoublyLinkedList import *


class LinkedStack:

    def __init__(self):
        self.dll = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.dll.add_last(e)

    def top(self):
        if self.is_empty():
            raise "Empty Stack"
        return self.dll.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise "Empty Stack"
        val = self.dll.trailer.prev.data
        self.dll.delete_last()
        return val
