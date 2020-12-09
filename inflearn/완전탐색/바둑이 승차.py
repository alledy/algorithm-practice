arr = [81,58,42,33,61]
c = 259
result = -2147000000

def DFS(d,s):
    global result
    if s > c:
        return
    if d == len(arr):
        if s > result:
            result = s
    else:
        DFS(d+1, s+arr[d])
        DFS(d+1, s)
    

DFS(0,0)
print(result)

"""
처음에 이 문제는 그리디라고 생각했다. 무거운 원소부터 채우면 되는거 아닌가 싶었는데, 제한이 18인데 [10, 9, 9] 인 경우
10을 넣고 나면 나머지를 넣을 수가 없는 반면, 
9를 2개 넣으면 18이 된다. 
그러므로 이건 모든 경우의 수를 따져서 넣는 방법으로 해야 정답을 구할 수 있다.
"""