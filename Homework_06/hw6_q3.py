from DoublyLinkedList import *


class CompactString:
    def __init__(self, orig_str):
        self.dll = DoublyLinkedList()
        if len(orig_str) > 0:
            count = 1
            for i in range(1, len(orig_str)):
                if orig_str[i] == orig_str[i-1]:
                    count += 1
                else:
                    self.dll.add_last((orig_str[i-1], count))
                    count = 1
            self.dll.add_last((orig_str[-1], count))

    def __add__(self, other):
        res = CompactString('')
        cursor = self.dll.header.next
        while cursor.data is not None:
            res.dll.add_last(cursor.data)
            cursor = cursor.next
        cursor = other.dll.header.next
        if self.dll.trailer.prev.data[0] == other.dll.header.next.data[0]:
            res.dll.trailer.prev.data = (res.dll.trailer.prev.data[0],
                                         res.dll.trailer.prev.data[1] + other.dll.header.next.data[1])
            cursor = cursor.next
        while cursor.data is not None:
            res.dll.add_last(cursor.data)
            cursor = cursor.next
        return res

    def __eq__(self, other):
        if len(self.dll) != len(other.dll):
            return False
        cursor_1 = self.dll.header.next
        cursor_2 = other.dll.header.next
        while cursor_1.data is not None:
            if cursor_1.data != cursor_2.data:
                return False
            cursor_1 = cursor_1.next
            cursor_2 = cursor_2.next
        return True

    def __lt__(self, other):
        cursor_1 = self.dll.header.next
        cursor_2 = other.dll.header.next
        while (cursor_1.data is not None) & (cursor_2.data is not None):
            if cursor_1.data[0] > cursor_2.data[0]:
                return False
            elif cursor_1.data[0] < cursor_2.data[0]:
                return True
            if cursor_1.data[1] == cursor_2.data[1]:
                cursor_1 = cursor_1.next
                cursor_2 = cursor_2.next
            elif cursor_1.data[1] > cursor_2.data[1]:
                cursor_2 = cursor_2.next
            else:
                cursor_1 = cursor_1.next
        return len(self.dll) < len(other.dll)

    def __le__(self, other):
        if (self == other) | (self < other):
            return True
        return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return ', '.join([str(elem) for elem in self.dll])
    