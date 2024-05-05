from ArrayStack import *

lst = [1, -14, 5, 6, -7, 9, 10, -5, -8]
s = ArrayStack()
for i in lst:
    s.push(i)


def stack_sum(s):
    if s.is_empty():
        return 0
    return s.pop() + stack_sum(s)


print(stack_sum(s))