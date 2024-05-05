from ArrayStack import *


def eval_prefix(exp_str):
    operations = '+-*/'
    exp_lst = exp_str.split()
    s = ArrayStack()

    for i in exp_lst:

        if i in operations:
            s.push(i)

        if i.isdigit():
            arg2 = int(i)

            while not s.is_empty() and isinstance(s.top(), int):
                arg1 = s.pop()
                op = s.pop()

                if op == '+':
                    result = arg1 + arg2
                elif op == '-':
                    result = arg1 - arg2
                elif op == '*':
                    result = arg1 * arg2
                elif op == '/':
                    result = arg1 / arg2
                arg2 = result

            else:
                s.push(arg2)
    return s.pop()


print(eval_prefix('- + * 16 5 * 8 4 20'))