def calc(expr):
    if not expr:
        return 0
    expr = expr.split(' ')
    stack = []
    for n in expr:
        if n.isdigit() or '.' in n:
            stack.append(n)
        else:
            num = str(eval('{2}{1}{0}'.format(stack.pop(), n, stack.pop())))
            stack.append(num)
    return float(stack[-1]) if '.' in stack[-1] else int(stack[-1])


assert calc('5 1 2 + 4 * + 3 -') == 14
assert calc("") == 0
assert calc("1 2 3") == 3
assert calc("1 2 3.5") == 3.5
assert calc("1 3 +") == 4
assert calc("1 3 *") == 3
assert calc("1 3 -") == -2
assert calc("4 2 /") == 2
