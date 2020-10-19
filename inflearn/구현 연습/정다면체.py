"""
문제: 정N면체와 정M면체의 주사위를 던져서 나올 수 있는 합 중 가장 확률이 높은 숫자를 출력하시오
단, 정답이 여러 개일 경우 오름차순 출력
N과 M은 4, 6, 8, 12, 20 중 하나이다
"""

1 2 3 4
1 2 3 4 5 6 

4 * 6 = 24 가지 경우의 수

2 3 4 5
3 4 5 6
4 5 6 7
5 6 7 8 
6 7 8 9
7 8 9 10

..? 오또케 풀라능

규칙성
n 이 더 작거나 같다고 가정하면, 최대한 개수가 나오는 대각선은 n개짜리
n * n 이면 하나일거고 4 * 4 => 5 (즉 n + 1)
n * n + 1 이면 2개일거고 n + 1, n + 2
n + 2면 3개일 거고... n+1, n+2, n+3

if n <= m:
    c = m - n + 1 # 정답의 개수
    for i in range(1,c+1):
        print(n+i, end=' ')        
else:
    c = n - m + 1
    for i in range(1, c+1):
        print(m+i, end=' ')


####### 

max_n = n + m
arr = list(max_n+1) # [0] * max_n+1
for x in range(1, n+1):
    for y in range(1, m+1):
        arr[x+y] = arr[x+y] + 1 

max_frequency = max(arr)
for idx, x in enumerate(arr):
    if x == max_frequency:
        print(idx, end=' ')
    
    
"""
2중 포문으로 생각하기
list 초기화
"""