"""
문제
M개의 DVD, 모두 같은 길이, N개의 노래를 전부 녹화할 수 있는 최소 길이를 구하라
"""

def calc(arr, l):
    cnt, s = 0,0
    for x in arr:
        if s+x > l:
            cnt += 1
            s = x
        elif s+x == l:
            cnt += 1 
            s = 0
        else:
            s += x
    if s > 0:
        cnt += 1
    return cnt
        

# 최대한의 길이가 sum(arr)을 넘지는 않을거고
def solution(arr, n, m):
    ans = 0
    s, e = 1, sum(arr)
    while s <= e:
        l = (s+e)//2
        if l < max(arr):
            s = l+1
            continue
        res = calc(arr,l)
        if res <= m:
            ans = l
            e = l-1
        else:
            s = l+1
    return ans


"""
만약 l이 5 같은 숫자로 설정되는 경우에는, 한곡도 담을 수가 없는 상황이 생긴다. 
그런 케이스를 고려하지 않아서 무한루프가 도는 경우가 있다
"""