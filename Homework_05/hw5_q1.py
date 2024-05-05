from ArrayStack import ArrayStack

var_dict = {}


def is_operator(val):
    return val in ['+', '-', '*', '/']


def to_digit(val):
    if isinstance(val, int):
        return val
    elif val.isdigit():
        return int(val)
    else:
        return var_dict[val]


def main():
    while 1:
        s = ArrayStack()
        var_name = None
        expr = input('-->')
        if expr == 'done()':
            return
        expr = expr.split()
        if len(expr) == 1:
            print(to_digit(expr[0]))
            continue
        if expr[1] == '=':
            var_name = expr[0]
            expr.pop(0), expr.pop(0)
        for opt in expr:
            if is_operator(opt):
                n1, n2 = to_digit(s.pop()), to_digit(s.pop())
                if opt == '+':
                    res = n2 + n1
                elif opt == '-':
                    res = n2 - n1
                elif opt == '*':
                    res = n2 * n1
                elif opt == '/':
                    res = n2 / n1
                s.push(res)
            else:
                s.push(opt)
        if var_name is not None:
            var_dict[var_name] = s.top()
            print(var_name)
        else:
            print(s.top())


if __name__ == '__main__':
    main()
