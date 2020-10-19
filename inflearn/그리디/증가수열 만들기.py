# 좌 또는 우에서만 숫자를 가져갈 수 있다.
# 가져간 숫자로 증가 수열을 만든다. 
# 최대 증가 수열의 길이와, 왼쪽에서 빼갔는지 오른쪽에서 빼갔는지를 기록한다 
from collections import deque
def solution(n, arr):
    arr = deque(arr)
    ans = []
    res = [-1] 
    while arr:
        last = res[-1]
        if last > arr[0] and last > arr[-1]:
            break
        elif last > arr[0] and last < arr[-1]:
            ans.append("R")
            res.append(arr.pop())
        elif last < arr[0] and last > arr[-1]:
            ans.append("L")
            res.append(arr.popleft())
        else:
            if arr[0] < arr[-1]:
                ans.append("L")
                res.append(arr.popleft())
            else:
                ans.append("R")
                res.append(arr.pop())
    
    return ans
        
