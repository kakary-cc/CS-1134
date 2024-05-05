from DoublyLinkedList import *


class Integer:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        for i in num_str:
            self.dll.add_last(int(i))
        # Remove Leading Zeros
        while (len(self.dll) > 1) & (self.dll.header.next.data == 0):
            self.dll.delete_first()

    def __add__(self, other):
        res = Integer('')
        if len(self.dll) > len(other.dll):
            long = self
            short = other
        else:
            short = self
            long = other
        s_cursor = short.dll.trailer.prev
        for _ in range(len(short.dll)):
            res.dll.add_first(s_cursor.data)
            s_cursor = s_cursor.prev
        l_cursor = long.dll.trailer.prev
        res_cursor = res.dll.trailer.prev
        carry = 0
        for _ in range(len(long.dll)):
            if isinstance(res_cursor.data, int):
                res_cursor.data += l_cursor.data + carry
            else:
                res_cursor = res.dll.add_first(l_cursor.data + carry)
            carry = res_cursor.data // 10
            res_cursor.data %= 10
            res_cursor = res_cursor.prev
            l_cursor = l_cursor.prev
        if carry:
            res.dll.add_first(1)
        return res

    def __repr__(self):
        out = ""
        for i in self.dll:
            out += str(i)
        return out

    def __mul__(self, other):
        res = Integer('')
        if int(str(self)) == 0:
            res.dll.add_last(0)
            return res
        for i in range(int(str(self))):
            res = res + other
        return res