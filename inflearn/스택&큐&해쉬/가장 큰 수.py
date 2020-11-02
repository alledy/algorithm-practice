
# 숫자의 순서가 유지됨
# 가장 크게 만들려면 '앞에' '큰숫자'가 있는게 중요함
# 앞에서부터 비교하면서 앞의 숫자 < 뒤의 숫자인 경우 pop
# pop한 개수가 m개 가 될 때까지 진행
# 만약 m개가 안된 경우 987654321 이렇게 되어있는 경우에는
# 마지막에 자르기

# pop을 하면, 포인터가 다음을 가르키지 않아야 하고

def biggest2(n,m):
    l = list(str(n))
    p = 1
    while p < len(l) and m > 0:
        if p == 0 or l[p-1] >= l[p]:
            p += 1
        elif l[p-1] < l[p]:
            l.pop(p-1)
            m -= 1
            p -= 1
        
    if m > 0:
        l = l[:-m]
    return int(''.join(l))

    
"""
for문을 쓰지 않았어야 함
while 문에 and를 썼어야 함
"""        

def biggest3(n,m):
    stack = []
    l = list(str(n))
    for x in l:
        while stack and m > 0 and stack[-1] < x:
            stack.pop()
        stack.append(x)
    if m > 0:
        stack = stack[:-m]
    return int(''.join(stack))
    
"""
첫 번째 풀이 때는 스택이라는 자료 구조를 사용했다고 볼 수 없음. 
조건에 충족하는 한 뒤에서 pop하고 아니면 append하는 조건 -> stack을 이용할 생각을 했었어야.
"""
    
            
    
