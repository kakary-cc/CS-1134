from DoublyLinkedList import *


class MidStack:

    def __init__(self):
        self.dll = DoublyLinkedList()
        self.mid_node = self.dll.header

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.dll.add_last(e)
        if len(self) % 2:
            self.mid_node = self.mid_node.next

    def top(self):
        if self.is_empty():
            raise "Empty Stack"
        return self.dll.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise "Empty Stack"
        val = self.dll.trailer.prev.data
        self.dll.delete_last()
        if len(self) % 2:
            self.mid_node = self.mid_node.prev
        return val

    def mid_push(self, e):
        self.dll.add_after(self.mid_node, e)
        if len(self) % 2:
            self.mid_node = self.mid_node.next

    def get_mid(self):
        return self.mid_node.data


ms = MidStack()
ms.push(2)
ms.push(4)
ms.push(6)
ms.push(8)
ms.push(10)
ms.mid_push(12)
