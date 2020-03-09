"""
n: 입국심사 받는 사람의 수
times: 각 검사관이 검사하는 데 걸리는 시간 배열
"""

"""
right는 검사시간이 가장 오래 걸리는 사람이 n명을 모두 심사했을 때 걸리는 시간 = 최대 시간
done 은 주어진 시간 내에서 최대한 심사할 수 있는 사람의 수
"""

def solution(n, times):
    right = max(times) * n
    left = 0
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        done = 0
        for time in times:
            done += mid // time
        if done < n:
            left = mid + 1 
        else:
            right = mid - 1
            answer = mid
        
    return answer
        
        
        
            
    