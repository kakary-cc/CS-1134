from ArrayStack import *


class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.max_val = None

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.stack.push((val, self.max_val))
        if isinstance(self.max_val, int):
            self.max_val = max(self.max_val, val)
        else:
            self.max_val = val

    def top(self):
        return self.stack.top()[0]

    def pop(self):
        val = self.stack.pop()
        if self.is_empty():
            self.max_val = None
        else:
            self.max_val = val[1]
        return val[0]

    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.max_val


def test():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    print(maxS.pop())
    print(maxS.pop())
    print(maxS.max())


# if __name__ == '__main__':
#     test()
