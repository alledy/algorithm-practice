def steal_bar(bars):
    stack = []
    cnt = 0
    for i,x in enumerate(bars):
        if x == '(':
            stack.append(1)
        else:
            if bars[i-1] == '(':
                stack.pop()
                stack = [y+1 for y in stack] 
            else:
                cnt += stack.pop()
    return cnt

    """
    stack = [y+1 for y in stack]
    이렇게 하는 것보다 cnt += len(stack)
    하고 else문에서 cnt +=1 
    이렇게 해주는 게 더 빠른 방법
    """ 
            


        