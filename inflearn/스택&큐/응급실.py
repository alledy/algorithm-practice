# arr은 전체 위험도가 담긴 num[]
# m은 m번째 인덱스 환자가 몇번째로 치료를 받는지 구해야 하는 것
import heapq
def emergency(arr,m):
    h = []
    for i, x in enumerate(arr):
        heapq.heappush(h,(-x, i))
    cnt = 0
    while h:
        cnt += 1 
        tmp = heapq.heappop(h)
        if tmp[1] == m:
            return cnt
    
                    
"""
왜 우선순위 큐로는 안되는걸까?
처음엔 줄서기 + 우선순위가 있으니 우선순위 큐 아냐?! 라고 생각했는데, 
생각해보니 줄선대로 나오지 않는다. 같은 우선순위에 대해서 빨리 온 사람이 빨리 나가지 않음. 
그러므로 우선순위 큐를 사용할 수 없다. 
"""

from collections import deque
def emergency1(arr,m):
    dq = deque([])
    cnt = 0
    for i, x in enumerate(arr):
        dq.append((x,i))
    while dq:
        first = dq.popleft()
        for i, x in enumerate(dq):
            # 위험도가 더 큰 환자가 나온다면
            if x[0] > first[0]:
                dq.append(first)
                tmp = i
                while tmp:
                    tmp -= 1
                    dq.append(dq.popleft())
                break
        else:
            # for문을 다 돌았는데 위험도 가 더 큰 환자가 없다
            cnt += 1
            if first[1] == m:
                return cnt
                
def emergency2(arr,m):
    dq = deque([])
    cnt = 0
    for i, x in enumerate(arr):
        dq.append((x,i))
    while dq:
        first = dq.popleft()
        # any를 이용해서 조금 더 깔끔하게
        if any(first[0] < x[0] for i,x in enumerate(dq)):
            dq.append(first)
            while i:
                dq.append(dq.popleft())
                i -= 1
        else:
            cnt += 1
            if first[1] == m:
                return cnt

                
            
            
            
        
    
    


    
    