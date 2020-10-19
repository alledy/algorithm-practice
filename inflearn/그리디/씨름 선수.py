"""
각 선수의 키와 몸무게는 모두 다릅니다
씨름 선수로 뽑히는 최대 인원을 출력
"""

def solution(arr,n):
    # arr은 2차 배열
    i = 0
    while i < len(arr):
        for x in arr:
            if arr[i][0] < x[0] and arr[i][1] < x[1]:
                arr.pop(i)
                break
        else:
            i += 1 
    return len(arr)

solution([[172,67], [183,65], [180,70], [170,72], [181,60]],5)

# 이게 문제가 그리디니까 다시 풀어봄

def solution2(arr,n):
    arr.sort(key=lambda x: x[0])
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][1] < arr[j][1]:    
                break
        else:
            cnt += 1
    return cnt
    
