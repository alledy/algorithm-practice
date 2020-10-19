"""
문제: n개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중 s번째부터 e번째까지의 수를 
오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력하시오
"""

# 원소가 n개인 배열 arr

split_arr = arr[s:e+1]
split_arr.sort()
print(split_arr[k-1])

T = int(input()) # 테스트케이스 수
for t in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split())
    arr = arr[s-1:e]
    arr.sort()
    print(arr[k-1])

"""
몇 번째 숫자, 인덱스... 크흠..
"""
    

