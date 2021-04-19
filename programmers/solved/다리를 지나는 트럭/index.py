# 먼저 들어간 트럭이 반드시 먼저 나오게 되어있다. 소요되는 시간이 모두 동일하니까.
# 그러므로 큐를 이용한다. 
# time이 1씩 증가한다. 
# time이 갱신될 때마다 다리 위에 weight을 recalculate한다. 
# 계산 결과, 현재 대기 트럭이 들어갈 수 있다면 들어간다. 
# 이 때 나오는 시간을 기록하는 큐에 넣는다. (out)
# 계산 결과, 대기 트럭이 들어갈 수 없다면 트럭이 들어갈 수 있는 시간까지 루프를 돈다. 
# 대기 트럭 배열이 모두 비게 되었을 때, out 큐에 있는 맨 마지막 녀석의 값이 답이 된다. 
from collections import deque

def solution(bridge_length, limit, trucks):
    TIME, WEIGHT = 0, 1
    out = deque([])
    weights, time, next_idx = 0, 0, 0 # next_idx는 지금 대기 중인 트럭 idx
    
    while next_idx < len(trucks):
        time += 1
        
        # recalculate
        if out and out[0][TIME] == time:
            weights -= out.popleft()[WEIGHT]
            
        # if next truck can go
        if trucks[next_idx] + weights <= limit:
            weights += trucks[next_idx]
            out.append((time + bridge_length, trucks[next_idx]))
            next_idx += 1
        
    return out[-1][TIME]