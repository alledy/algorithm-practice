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