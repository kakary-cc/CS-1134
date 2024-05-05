from ArrayStack import *


class Queue:
    def __init__(self):
        self.s1 = ArrayStack()
        self.s2 = ArrayStack()

    def __len__(self):
        return len(self.s1) + len(self.s2)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, val):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s2.push(val)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.s1.top()

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.s1.pop()


# sq = Queue()
# for i in range(1, 6):
#     sq.enqueue(i)