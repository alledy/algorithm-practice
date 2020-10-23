def postfix_calc(p):
    stack = []
    for x in p:
        if x.isdecimal():
            stack.append(x)
        else:
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            res = 0
            if x == '*':
                res = tmp2 * tmp1
            elif x == '/':
                res = tmp2 / tmp1
            elif x == '+':
                res = tmp2 + tmp1
            elif x == '-':
                res = tmp2 - tmp1
            stack.append(res)
    return stack.pop()
                 