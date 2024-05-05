class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):
        new_node = SinglyLinkedList.Node(val, None)
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_before(self, node, val):
        cursor = self.header
        while cursor.next is not node:
            cursor = cursor.next
        return self.add_after(cursor, val)

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_before(None, val)

    def delete_node(self, node):
        next_node = node.next
        cursor = self.header
        while cursor.next is not node:
            cursor = cursor.next
        cursor.next = next_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        cursor = self.header
        while cursor.next is not None:
            cursor = cursor.next
        cursor.next = None
        self.size -= 1
        data = cursor.data
        cursor.disconnect()
        return data

    def __iter__(self):
        cursor = self.header.next
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " --> ".join([str(elem) for elem in self]) + "]"


sll = SinglyLinkedList()
