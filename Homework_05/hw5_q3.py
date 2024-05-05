from ArrayStack import *
from ArrayDeque import *


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if self.is_empty():
            self.stack.push(val)
        else:
            self.deque.enqueue_last(val)
            if len(self.deque) > len(self.stack):
                self.stack.push(self.deque.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        elif len(self) == 1:
            return self.stack.top()
        else:
            return self.deque.last()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        elif len(self) == 1:
            return self.stack.pop()
        else:
            val = self.deque.dequeue_last()
            if len(self.stack) - len(self.deque) > 1:
                self.deque.enqueue_first(self.stack.pop())
            return val

    def mid_push(self, val):
        self.deque.enqueue_first(val)


def test():
    midS = MidStack()
    midS.push(2)
    midS.push(4)
    midS.push(6)
    midS.push(8)
    midS.push(10)
    midS.mid_push(12)
    for i in range(6):
        print(midS.pop())


# if __name__ == '__main__':
#     test()
