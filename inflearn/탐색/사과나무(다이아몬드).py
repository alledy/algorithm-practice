"""
문제 
n*n 인 정사각형이 있다. n은 반드시 홀수이다. (3~20)
다이아몬드 모양으로 꽉차게 색칠할 때, 색칠되는 칸에 들어있는 숫자 총합을 구하라
"""

# n*n 행렬

# 시작점, 끝점 n // 2
# 이걸 기준으로 하나씩 내려갈수록 시작점 -1, 끝점 +1

def solution(arr, n):
    # arr는 n차원 배열
    answer = 0
    s, e = n//2, n//2
    for i in range(n):
        for j in range(s, e+1):
            answer += arr[i][j]
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    return answer    