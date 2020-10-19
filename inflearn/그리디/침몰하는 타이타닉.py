def solution(arr, n, m):
    # arr은 n 길이
    # m은 보트의 kg 제한
    arr.sort()
    cnt = 0
    while len(arr) > 0:
        cv = arr.pop(0)
        cnt += 1
        tmp = -1
        for idx, x in enumerate(arr):
            if x <= m-cv:
                tmp = idx
            else:
                break
        if tmp != -1:
            arr.pop(tmp)
    return cnt        

solution([90,50,70,100,60], 5, 140)

# 그리디
# 뚱뚱한 사람부터 소팅한 다음, 가장 마른 사람이랑 탈 수 있는지 본다
# 탈 수 있다면 타고, 아니면 혼자 탄다
def solution2(arr, n, m):
    cnt = 0
    arr.sort(reverse=True)
    while arr:
        if len(arr) == 1:
            arr.pop()
        if arr[0] + arr[-1] <= m:
            arr.pop(0)
            arr.pop()
        else:
            arr.pop(0)
        cnt += 1
    return cnt
            
            
    
from collections import deque

def solution3(arr, n, m):
    arr.sort()
    arr = deque(arr) # arr는 deque가 된다
    cnt = 0
    while arr:
        if len(arr) == 1:
            cnt += 1
            break
        if arr[0] + arr[-1] > m:
            arr.pop()
            cnt += 1
        else:
            arr.popleft()
            arr.pop()
            cnt += 1
    return cnt

