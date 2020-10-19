"""문제
n개 길이인 arr을 오름차순 정렬한 다음 그 중 한 원소인 m이 몇번째 위치인지 출력
"""
def solution(arr, n, m):
    arr.sort()
    s, e = 0, n-1 
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] == m:
            return mid + 1
        elif arr[mid] > m:
            e = mid - 1
        elif arr[mid] < m:
            s = mid + 1
        
        