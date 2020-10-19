def solution(n, arr):
    # arr은 n*n 2차원 배열
    ms = 0
    for x in range(n):
        s = 0
        for y in range(n):
            s += arr[x][y]
        if ms < s:
            ms = s
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[j][i]
        if ms < s:
            ms = s    
    s = 0
    for i in range(n):
        s += arr[i][i]
    if ms < s:
        ms = s
    s = 0
    for i in range(n):
        s += arr[i][n-i-1]
    if ms < s:
        ms = s
    return ms

###

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # a는 2차원 배열
def solution2(arr, n):
    largest = 0
    for i in range(n):
        sum1=sum2=0
        for j in range(n):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2    
           
                
"""
이런식으로 한번에..
"""