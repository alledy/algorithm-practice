"""문제
N개로 된 수열이 있다. 
i 번째부터 j 번째까지의 수의 합이 M이 되는 경우의 수를 구하라
단 1부터 시작한다. 
"""

# 적게 돌 수 있는 방법 없을까


def solution(n, m , arr):
    answer = 0
    for i in range(n):
        sum = 0
        j = i
        while sum < m and j < n:
            sum += arr[j]
            if sum == m:
                answer += 1
                j += 1 
                break
            elif sum > m:
                break
            else:
                j += 1 
        if j == n:
            break
    return answer

"""
부분합 구하는 문제
슬라이딩 윈도우?
"""

def solution2(n, m, arr):
    left, right, answer = 0,1,0
    total = arr[0]
    while right < n:
        if total < m:
            total += arr[right]
            right += 1
        if total == m:
            answer += 1
            total -= arr[left]
            left += 1
        if total > m:
            total -= arr[left]
            left += 1
    if total == m:
        answer += 1
    return answer


        
            
            
    